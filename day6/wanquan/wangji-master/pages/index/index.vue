<template>
	<view class="backg">
		<!-- <view>
			<view class="item" v-for="(item,index) in questionAndAnswers" :key="index">
				<view class="qustion">{{item.question}}</view>
				<view class="author">{{item.answers[0].author}}</view>
				<view class="answer">{{item.answers[0].answer_text.substring(0,20)+'...'}}</view>
			</view>
		</view> -->
		
		<!-- 顶部切换 -->
		
		<view>
			<swiper class="swiper" circular indicator-dots autoplay interval=2000>
				<swiper-item>
					<image class="imag" src="../../static/logo.png"></image>
				</swiper-item>
				
				<swiper-item>
					<image class="imag" src="../../static/zhihu/tabbar/about.png"></image>
				</swiper-item>
				
				<swiper-item>
					<image class="imag" src="../../static/zhihu/tabbar/basics.png"></image>
				</swiper-item>
			</swiper>
			
		</view>
		
		<!-- 正文 -->
		
		<view class="content">
			
			<view class="submo">
				<view class="item" @click="click(index)" v-for="(item,index) in questionAndAnswers" :key="index">
					<image class="logo" :src="convert(index)"></image>
					<view class="qustion">{{item.question}}</view>
					<view class="author">{{item.answers[0].author}}</view>
				</view>
			</view>
		</view>
		
		<!-- 底部菜单 -->
		
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
		name:'zhihu',
		data() {
			
			return {
				questionAndAnswers:[],
				curPage:0
			}
		},
		onLoad() {
			console.log(questionAndAnswers)
			this.questionAndAnswers = questionAndAnswers
			uni.setNavigationBarTitle({
			    title: 'bilibili'
			});
		},
		created() {
			console.log(questionAndAnswers)
			this.questionAndAnswers = questionAndAnswers
		},
		methods: {
			
			click(index){
				console.log('zhihu',index)
				uni.navigateTo({
					url: '/pages/zhihu/browse?index='+index, // 参数名和值
				});
			},
			clickIcon(index){
				console.log(index)
				this.curPage = index;
			},
			convert(index){
				index = index%4+1
				return require('../../static/image/img'+ index +'.png')
			},
		}
	}
	
</script>

<style>
	.imag{
		display:flex;
		width:150px;
		height:150px;
		margin: auto;
	}
	.swiper{
		display: flex;
		width: 100vw;
		height: 200px;
	}
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
		width:100vw;
		flex-wrap:wrap;
	}
	.tabbar{
		display: flex;
		justify-content: space-around;
		height: 6vh;
		background-color: black; 
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
		color:white;
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
