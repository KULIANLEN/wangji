<template>
	<view class="backg">
		<!-- <view>
			<view class="item" v-for="(item,index) in questionAndAnswers" :key="index">
				<view class="qustion">{{item.question}}</view>
				<view class="author">{{item.answers[0].author}}</view>
				<view class="answer">{{item.answers[0].answer_text.substring(0,20)+'...'}}</view>
			</view>
		</view> -->
		
		<view class="content">
			
			<view class="submo">
				<view class="item" v-for="(item,index) in questionAndAnswers" :key="index">
					<image class="logo" :src="convert(index)"></image><view class="qustion">{{item.question}}</view>
					<view class="author">{{item.answers[0].author}}</view>
				</view>
			</view>
			
			
		</view>
		<view class="tabbar">
			<view class="row-container">
				<image v-if="curPage==1" class="icon" @click="clickIcon(1)" src="../../static/zhihu/tabbar/index_blue.svg"></image>
				<image v-else class="icon" @click="clickIcon(1)" src="../../static/zhihu/tabbar/index.svg"></image>
				<text class="text-area">首页</text>
			</view>
			
			<view class="row-container">
				<image v-if="curPage==2" class="icon" @click="clickIcon(2)" src="../../static/zhihu/tabbar/index_blue.svg"></image>
				<image v-else class="icon" @click="clickIcon(2)" src="../../static/zhihu/tabbar/index.svg"></image>
				<text class="text-area">动态</text>
			</view>
			
			<view class="row-container">
				<image v-if="curPage==3" class="icon" @click="clickIcon(3)" src="../../static/zhihu/tabbar/index_blue.svg"></image>
				<image v-else class="icon" @click="clickIcon(3)" src="../../static/zhihu/tabbar/index.svg"></image>
				<text class="text-area">会员购</text>
			</view>
			
			<view class="row-container">
				<image v-if="curPage==4" class="icon" @click="clickIcon(4)" src="../../static/zhihu/tabbar/index_blue.svg"></image>
				<image v-else class="icon" @click="clickIcon(4)" src="../../static/zhihu/tabbar/index.svg"></image>
				<text class="text-area">我的</text>
			</view>
		</view>
	</view>
</template>

<script>
	import questionAndAnswers from '../../data/zhihu/qa.json'
	export default {
		data() {
			return {
				questionAndAnswers:[],
				curPage:0
			}
		},
		onLoad() {
			console.log(questionAndAnswers)
			this.questionAndAnswers = questionAndAnswers
		},
		methods: {
			clickIcon(index){
				console.log(index)
				this.curPage = index;
			},
			convert(index){
				index = index%4+1
				return require('../../static/image/img'+ index +'.png')
			}
		}
	}
	
</script>

<style>
	.author{
		font-weight: 10;
		font-size: 14px;
	}
	.backg{
		background-color: #f0f0f0;
	}
	.submo{
		display: flex;
		align-items:center;
		justify-content: center;
		flex-wrap:wrap;
		border-style: ridge;
		border-color: rgba(255,255,255,0);
		/* border-color:#FFB6C1; */
	}
	.content {
		display: flex;
		align-items: center;
		justify-content: center;
		height: 74vh;
		flex-wrap:wrap;
	}
	.tabbar{
		display: flex;
		justify-content: space-around;
		height: 6vh;
		background-color: #8f8f94; 
		position:fixed;
		bottom:0px;
		width:100vw;
	}
	.icon{
		display: flex;
		width: 15vw;
		height: 15vw;
		
	}
	.logo {
		height: 300rpx;
		width: 360rpx;
		margin-top: 10rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
		flex-wrap:nowrap;
		border-top-left-radius: 10px;
		border-top-right-radius: 10px;
	}
	.row-container{
		display: flex;
		flex-direction: column;
		justify-content: center;
	}
	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}
	.item{
		display: flex;
		width: 46vw;
		height: 80vw;
		padding: 1vw;
		background-color: white;
		margin-top: -8vw;
		flex-direction: column;
		border-bottom-right-radius: 10px;
		border-bottom-left-radius: 10px;
	}
	.qustion{
		display: flex;
		font-size: 4vw;
		font-weight:500;
	}
</style>
