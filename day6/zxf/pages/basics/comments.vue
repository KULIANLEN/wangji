<template>
    <view class="container">
        <view class="comment-container">
            <view class="comment" v-for="(item) in vids[itemIdx].answers">
                <view class="comment-author">{{item.author}}</view>
                <view class="comment-content">{{item.answer_text}}</view>
            </view>
        </view>
        <view class="comment-adder">
            <view>
                <textarea v-model="commentAdderText" placeholder="输入评论内容"></textarea>
            </view>
            <button @click="pushComment('GUN GOD', commentAdderText)">
                发送
            </button>
        </view>
    </view>
</template>

<script>
export default{
    props:["vids", "itemIdx"],
    data(){
        return{
            commentAdderText:''
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
            console.log(this.vids[this.itemIdx].answers);
            this.commentAdderText='';
            this.$forceUpdate();
        },
    }
}
</script>

<style>
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
    padding-bottom: 5vw;
}
.comment-adder view{
    padding: 2vw;
    border: 1px;
    border-color: grey;
    border-style: solid;
    background-color: azure;
}
.comment-adder button{
    margin-top:2vw;
}
</style>