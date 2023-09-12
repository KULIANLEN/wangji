<template>
    <view class="container">
        <view class="title-wrap">
            <view class="title">{{vids[itemIdx].question}}</view>
        </view>
        <view class="image-wrap">
            <image :src="vids[itemIdx].thumbnail" mode="aspectFill"></image>
        </view>
        
        <swiper 
            class="extra"
        >
            <swiper-item class="relative">
                <view class="rel-vid" 
                v-for="(item, index) in relativeVids" :key="index"
                @click="openItem(item)">
                    <image :src="vids[item].thumbnail" mode="aspectFill"></image>
                    <view>
                        <view>
                            {{ vids[item].question }}
                        </view>
                    </view>
                </view>
            </swiper-item>
            <swiper-item class="comments">
                <comments :vids="vids" :itemIdx="itemIdx"></comments>
                
            </swiper-item>
        </swiper>
        
    </view>
</template>

<script>
import qa from 'data/zhihu/qa.json'
import comments from "@/pages/basics/comments.vue"
var time;
export default{
    data(){
        return{
            vids:[],
            itemIdx:0,
            relativeVids:[],
            commentAdderText:''
        }
    },
    onLoad(option){
        this.vids = qa;
        this.itemIdx = +option.idx;
		console.log(this.itemIdx);
        var indices = new Array(this.vids.length).fill(null).map((item, index)=>index);
        indices[this.itemIdx] = indices[indices.length-1];
        --indices.length;
        for(let i = 0; i < 10; ++i){
            let r = Math.floor(Math.random() * indices.length);
            this.relativeVids.push(indices[r]);
            indices[r] = indices[indices.length-1];
            --indices.length;
        }
		console.log(qa);
    },
    onShow(){
        
    },
    methods:{
        openItem(idx){
				uni.navigateTo({
					url: '/pages/basics/browse?idx='+idx
				});
			},
        pushComment(author, content){
            this.vids[this.itemIdx].answers.push(
                {
                    author: author,
                    answer_text: content
                }
            );
            this.commentAdderText='';
        },
    },
    components:{
        comments
    }
}
</script>

<style>
.title{
    font-size: 30px;
    font-weight: bold;
    margin: 5vw;
}
.image-wrap{
    display: flex;
    width: 100%;
    justify-content: center;
    margin-bottom: 5vh;
}
.extra{
    height:100vh;
}
.comments{
    overflow: scroll;
    height:1vh;
}
.comments::-webkit-scrollbar{
    display:none;
}
.relative{
    overflow: scroll;
    height:1vh
}
.relative::-webkit-scrollbar{
    display:none;
}
.rel-vid{
    display: flex;
    flex-direction: row;
    height: 13vh;
    padding: 1vh;
    border: 1px;
    border-style: solid;
    border-color: gray;
}
.rel-vid image{
    width: 15vh;
    height: 10vh;
}
.comments{
    border: 1px;
    border-style: solid;
    border-color: gray;
}
</style>