<template>
	<view>
		<image class='picture' :src="convert(showingIndex)"></image>
		<image class="jianjie" src="../../static/image/jianjie.png"></image>
		<view class="author">{{qestionAndAnswer[showingIndex].answers[0].author}}</view>
		<view class="qustion">{{qestionAndAnswer[showingIndex].question}}</view>
		<image class="yjsl" src="../../static/image/img11.png"></image>
		<image class="guanggao" src="../../static/image/guanggao.png"></image>
		<view class="answer"></view>
	</view>
</template>

<script>
	import qa from '../../data/zhihu/qa.json'
	export default {
		data() {
			return {
				qestionAndAnswer:[],
				showingIndex:0,
			}
		},
		
		onLoad() {
			
		},
		onShow() {
			this.qestionAndAnswer = qa
			console.log(this.qestionAndAnswer)
			this.showingIndex = this.$route.query.index;
			if(!this.showingIndex) this.showingIndex=0
			console.log(this.showingIndex)
		},
		methods: {
			convert(index){
				index = index%4+1
				return require('../../static/image/img'+ index +'.png')
			},
		}
	}
</script>

<style>
	.author{
		margin-left:5px;
	}
	.picture{
		display: flex;
		width: 100vw;
		height: 53vw;
	}
	.yjsl{
		display: flex;
		width:100vw;
		height: 90px;
	}
	.guanggao{
		display: flex;
		width:100vw;
		height:330px;
	}
	.jianjie{
		width:100vw;
		height:35px;
	}
</style>
