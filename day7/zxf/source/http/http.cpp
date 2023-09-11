#define CPPHTTPLIB_OPENSSL_SUPPORT
#include"httplib.h"
#include <icu.h>
#include<windows.h>
#include <iostream>
#include<fstream>

struct para_each {
    std::string str;
    para_each(std::string& s) :str(s) {
    }
    para_each(std::string&& s) :str(s){
    }
    struct it {
        para_each& p;
        size_t offset;
        size_t end_offset;
        it(para_each& p, size_t i) : p(p) {
            offset = p.str.find("<p>", i);
            end_offset = p.str.find("</p>", offset);
        }
        it(para_each& p) :p(p),offset(-1),end_offset(-1){}
        std::string operator *() const {
            auto ret = p.str.substr(offset + 3, end_offset - offset - 3);
            return ret;
        }
        it& operator++() {
            offset = p.str.find("<p>", end_offset+4);
            if(offset != -1)
                end_offset = p.str.find("</p>", offset);
            else {
                offset = end_offset = -1;
            }
            return *this;
        }
        bool operator==(it& rhs) {
            return &p == &rhs.p && offset == rhs.offset && end_offset == rhs.end_offset;
        }
        bool operator!=(it& rhs) {
            return &p != &rhs.p || offset != rhs.offset || end_offset != rhs.end_offset;
        }
    };
    it begin() {
        return it(*this, 0);
    }
    it end() {
        return it(*this);
    }
};

struct iobject {
    virtual std::string str(int level = 0) = 0;
};

struct sq_para : iobject {
    std::vector<std::unique_ptr<iobject>> content;
    sq_para(){}
    void push(iobject* obj) {
        content.push_back(std::unique_ptr<iobject>(obj));
    }
    std::string str(int level = 0) override {
        std::string ret;
        ret.resize(ret.size() + level, '\t');
        ret.append("[\n");
        for (auto& e : content) {
            ret.append(e->str(level + 1));
            ret.append(",\n");
        }
        if (content.size()) {
            ret.pop_back();
            ret.pop_back();
        }
        ret.push_back('\n');
        ret.resize(ret.size() + level, '\t');
        ret.push_back(']');
        return ret;
    }
};
struct cl_para : iobject {
    std::vector<std::unique_ptr<iobject>> content;
    cl_para(){}
    void push(iobject* obj) {
        content.push_back(std::unique_ptr<iobject>(obj));
    }
    std::string str(int level = 0) override {
        std::string ret;
        ret.resize(ret.size() + level, '\t');
        ret.append("{\n");
        for (auto& e : content) {
            ret.append(e->str(level + 1));
            ret.append(",\n");
        }
        if (content.size()) {
            ret.pop_back();
            ret.pop_back();
        }
        ret.push_back('\n');
        ret.resize(ret.size() + level, '\t');
        ret.push_back('}');
        return ret;
    }
};
struct kv_pair : iobject {
    std::unique_ptr<iobject> first;
    std::unique_ptr<iobject> second;
    kv_pair(iobject* first, iobject* second) : first(first),second(second) {};
    std::string str(int level = 0) override {
        std::string ret;
        ret.resize(ret.size() + level, '\t');
        ret.push_back('\"');
        ret.append(first->str());
        ret.append("\":\"");
        ret.append(second->str());
        ret.push_back('\"');
        return ret;
    }
};
struct jstr : iobject {
    std::string raw;
    jstr(std::string s):raw(s){}
    jstr(const char* s) :raw(s) {}
    std::string str(int level = 0) override {
        std::string ret;
        for (auto c : raw) {
            if (c == '\"')
                ret.append("\\\"");
            else
                ret.push_back(c);
        }
        return ret;
    }
};

std::string UTF82Local(std::string in) {
    UErrorCode status{ U_ZERO_ERROR };
    size_t enough_size = 4 * in.size();
    char* sp_buf = new char[enough_size];

    int len = ucnv_convert(NULL, "UTF8", sp_buf, enough_size, in.c_str(), in.size(), &status);
    std::string ret(sp_buf);
    delete[] sp_buf;
    return ret;
}
std::string Local2UTF8(std::string in) {
    UErrorCode status{ U_ZERO_ERROR };
    size_t enough_size = 4 * in.size();
    char* sp_buf = new char[enough_size];

    int len = ucnv_convert("UTF8", NULL, sp_buf, enough_size, in.c_str(), in.size(), &status);
    std::string ret(sp_buf);
    delete[] sp_buf;
    return ret;
}
void do_some_weird_transformation(std::string& str) {
    size_t idx = 0;
    while ((idx = str.find("&#", idx)) != -1) {
        size_t n_end = str.find(';', idx);
        char asc_s = std::atoi(str.substr(idx + 2, n_end - idx - 2).c_str());
        auto nstr = str.substr(0, idx);
        nstr.push_back(asc_s);
        str = nstr.append(str.substr(n_end + 1, str.length() - n_end - 1));
    }
}
int main()
{
    std::string path = "book.douban.com";
    httplib::SSLClient cli(path);
    auto headers = httplib::Headers();
    headers.insert(std::make_pair("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"));
    headers.insert(std::make_pair(
    "cookie",
    "bid=bzv--Bz3eGQ; _pk_id.100001.8cb4=0fac0a609949e80e.1691075918.; douban-fav-remind=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1692834014%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; __utma=30149280.26344112.1691075918.1691075918.1692834015.2; __utmz=30149280.1692834015.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=9XIl0dY3egIruYoSXzbubzYNx50Jgosx; ap_v=0,6.0; viewed=\"6872578_6272578_36483883\"; apiKey=; dbcl2=\"274360339:hFU2tUDMRYU\"; ck=NIpR; frodotk_db=\"3cef091978d64bdab6cd1b4c6a82e38e\"; push_noty_num=0; push_doumail_num=0"
    ));
    UINT64 first_id = 6872578;
    sq_para book_list;

    for (int i = 0; i < 30; ++i) {
        auto res = cli.Get(std::string() + "https://book.douban.com/subject/" + std::to_string(first_id + i) + "/", headers);
        auto book_info = new cl_para();
        std::string text = res->body;
        {
            size_t headLength = sizeof("<span property=\"v:itemreviewed\">") - 1;
            size_t idx = text.find("<span property=\"v:itemreviewed\">");
            size_t eidx = text.find("</span>", idx);
            std::string t = text.substr(idx + headLength, eidx - idx - headLength);
            do_some_weird_transformation(t);
            std::cout << UTF82Local(t) << std::endl;
            book_info->push(new kv_pair(new jstr("book_name"), new jstr(t)));
        }
        {
            size_t headLength = sizeof("<div class=\"intro\">");
            size_t idx = text.find("<div class=\"intro\">");
            if (idx != -1) {
                size_t eidx = text.find("</div>", idx);
                std::string ps = text.substr(idx + headLength, eidx - idx - headLength);
                auto pe = *para_each(std::string(ps)).begin();
                do_some_weird_transformation(pe);
                std::cout << UTF82Local(pe) << std::endl;
                book_info->push(new kv_pair(new jstr("introduction"), new jstr(pe)));
            }
            else {
                std::cout << "暂无简介" << std::endl;
                book_info->push(new kv_pair(new jstr("introduction"), new jstr(Local2UTF8("暂无简介"))));
            }
        }
        book_list.push(book_info);
    }
    std::fstream fs(fopen("books.json", "w"));
    fs << book_list.str();
    fs.close();
    system("pause");
}
