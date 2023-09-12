<template>
    <view class="container">
        <view class="title-wrap">
            <view class="title">{{vids[itemIdx].question}}</view>
        </view>
        <view class="comment-container">
            <view class="comment" v-for="(item) in vids[itemIdx].answers">
                <view class="comment-author">{{item.author}}</view>
                <view class="comment-content">{{item.answer_text}}</view>
            </view>
        </view>
        <view class="comment-adder">
            <textarea class="comment-adder-text" v-model="commentAdderText" placeholder="输入评论内容">

            </textarea>
            <button @click="pushComment('GUN GOD', commentAdderText)">
                发送
            </button>
        </view>
    </view>
</template>

<script>
import qa from 'data/zhihu/qa.json'
function f(a){
    console.log(a);
}
export default{
    data(){
        return{
            vids:[],
            itemIdx:0,
            query:uni.createSelectorQuery(),
            commentAdderText:''
        }
    },
    onLoad(){
        this.vids = qa;
        this.itemIdx = this.$route.query['idx'];
        if(this.itemIdx === undefined){
            this.itemIdx = 0;
        }
    },
    methods:{
        pushComment(author, content){
            console.log(content);
            this.vids[this.itemIdx].answers.push(
                {
                    author: author,
                    answer_text: content
                }
            );
            this.commentAdderText='';
        },
    }
}
</script>

<style>
.title{
    font-size: 30px;
    font-weight: bold;
    margin: 5vw;
}
.comment{
    margin:5vw;
}
.comment-author{
    margin-left: 5vw;
    font-size: 20px;
    margin-bottom: 3vw;
}
.comment-adder{
    margin: 5vw;
    border: 3px;
    border-color: black;
    background-color: azure;
}
</style>