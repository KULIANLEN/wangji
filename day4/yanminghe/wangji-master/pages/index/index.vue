<template>
	<view class="backg">
		<view class="hhh">	
			<nav class="navbar">
			  <div class="container">
				<div class="logo1">bilbii</div>
				<ul class="nav-links">
				  <li><a href="#">首页</a></li>
				  <li><a href="#">推荐</a></li>
				  <li><a href="#">视频</a></li>
				  <li><a href="#">游戏</a></li>
				  <li><a href="#">音乐</a></li>
				  <li><a href="#">动画</a></li>
				</ul>
				<div class="search-bar">
				  <input type="text" placeholder="搜索">
				  <button><i class="fa fa-search"></i></button>
				</div>
			  </div>
			</nav>
		</view>
		<swiper class="swiper" circular indicator-dots autoplay interval=3000>
			<swiper-item>
				<image class='pic' src="../../static/image/img1.png"></image>
			</swiper-item>
			
			<swiper-item>
				<image class='pic' src="../../static/image/img2.png"></image>
			</swiper-item>
			
			<swiper-item>
				<image class='pic' src="../../static/image/img3.png"></image>
			</swiper-item>
		</swiper>
		<view class="content">
			
			<view class="submo">
				<view class="item" @click="click(index)" v-for="(item,index) in questionAndAnswers" :key="index">
					<image class="logo" :src="convert(index)"></image>
					<view class="qustion">{{item.question}}</view>
					<view class="author">{{item.answers[0].author}}</view>
				</view>
			</view>
			
			
		</view>
		<view class="tabbar">
			<view class="row-container">
				<image v-if="curPage==1" class="icon" @click="clickIcon(1)" src="../../static/zhihu/tabbar/index_blue.svg"></image>
				<image v-else class="icon" @click="clickIcon(1)" src="../../static/zhihu/tabbar/index.svg"></image>
				<text class="text-area" @click="clickIcon(1)">首页</text>
			</view>
			
			<view class="row-container">
				<image v-if="curPage==2" class="icon" @click="clickIcon(2)" src="../../static/zhihu/tabbar/index_blue.svg"></image>
				<image v-else class="icon" @click="clickIcon(2)" src="../../static/zhihu/tabbar/index.svg"></image>
				<text class="text-area" @click="clickIcon(2)">动态</text>
			</view>
			
			<view class="row-container">
				<image v-if="curPage==3" class="icon" @click="clickIcon(3)" src="../../static/zhihu/tabbar/index_blue.svg"></image>
				<image v-else class="icon" @click="clickIcon(3)" src="../../static/zhihu/tabbar/index.svg"></image>
				<text class="text-area" @click="clickIcon(3)">会员购</text>
			</view>
			
			<view class="row-container">
				<image v-if="curPage==4" class="icon" @click="clickIcon(4)" src="../../static/zhihu/tabbar/index_blue.svg"></image>
				<image v-else class="icon" @click="clickIcon(4)" src="../../static/zhihu/tabbar/index.svg"></image>
				<text class="text-area" @click="clickIcon(4)">我的</text>
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
			console.log(questionAndAnswers),
			this.questionAndAnswers = questionAndAnswers,
			uni.setNavigationBarTitle({
				title:'bilibili'
			});
		},
		methods: {
			
			clickIcon(index){
				console.log(index)
				this.curPage = index;
			},
			convert(index){
				index = index%4+1
				return require('../../static/image/img'+ index +'.png')
			},
			
			click(index){
				console.log('zhihu',index)
				uni.navigateTo({
					url: '/pages/zhihu/browse?index='+index, // 参数名和值
				});
			}
			
		}	
	}
	
</script>

<style>
	.pic{
		display: flex;
		height:300px;
		width: 100vw;
	}
	.author{
		font-weight: 10;
		font-size: 14px;
		margin-top: 10rpx;
		margin-left: 20rpx;
		margin-right: 20rpx;
		margin-bottom: 50rpx;
		
	}
	.backg{
		background-color: #f0f0f0;
	}
	.submo{
		display: flex;
		align-items:center;
		justify-content: space-around;
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
		margin-top: 30px;
	}
	.tabbar{
		display: flex;
		justify-content: space-around;
		height: 6vh;
		background-color: #8f8f94; 
		position:fixed;
		bottom:0px;
		width:100vw;
		background-color: aliceblue;
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
		margin-left: 5rpx;
		margin-right: 50rpx;
		margin-bottom: 50rpx;
		flex-wrap:nowrap;
		border-top-left-radius: 10px;
		border-top-right-radius: 10px;
		font-family:  Comic Sans MS,
	}
	.row-container{
		display: flex;
		flex-direction: column;
		justify-content: center;
		background-color: #f0f0f0;
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
		background-color: #8f8f94;
	}
	.qustion{
		display: flex;
		font-size: 4vw;
		font-weight:500;
		
		margin-left: 20rpx;
		margin-right: 20rpx;
		margin-bottom: 20rpx;
	}
	.swiper{
		display: flex;
		margin-top: 0px;
		height: 200px;
		padding: 0%;
	}
	.navbar {
	  background-color: #00a1d6;
	  color: #fff;
	  transition: background-color 0.3s;
	  height: 50px;
	  
	}
	
	.navbar:hover {
	  background-color: #008bbf;
	}
	
	.container {
	  display: flex;
	  align-items: flex-start;
	  justify-content: flex-start;
	  padding: 0px 10px;
	}
	
	.logo1 {
	  font-size: 20px;
	  font-weight: bold;
	  transition: color 0.3s;
	  padding: 10px;
	}
	
	.logo:hover {
	  color: #f0f0f0;
	}
	
	.nav-links {
	  list-style: none;
	  display: flex;
	  padding: 5px;
	}
	
	.nav-links li {
	  margin-right: 20px;
	  transition: transform 0.3s;
	}
	
	.nav-links li:hover {
	  transform: scale(1.1);
	}
	
	.nav-links a {
	  color: #fff;
	  text-decoration: none;
	  transition: color 0.3s;
	}
	
	.nav-links a:hover {
	  color: #f0f0f0;
	  text-decoration: underline;
	}
	
	.search-bar {
	  display: flex;
	  align-items: center;
	}
	
	.search-bar input[type="text"] {
	  padding: 5px;
	  border-radius: 5px;
	  border: none;
	}
	
	.search-bar button {
	  background-color: transparent;
	  border: none;
	  color: #fff;
	  cursor: pointer;
	  margin-left: 5px;
	  transition: transform 0.3s;
	}
	
	.search-bar button:hover {
	  transform: rotate(360deg);
	}
	
	/* 使用 Font Awesome 图标 */
	.fa-search:before {
	  content: "\f002";
	  font-family: FontAwesome;
	}
	
	
</style>
