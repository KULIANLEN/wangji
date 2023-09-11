<template>
	<!--
	<view>
		<view class="item" v-for="(item,index) in questionAndAnswers" :key="index">
			<view class="qustion">{{item.question}}</view>
			<view class="author">{{item.answers[0].author}}</view>
			<view class="answer">{{item.answers[0].answer_text.substring(0,20)+'...'}}</view>
		</view>
	</view>
	-->
	<view>
		<view class="top">
			<view style="display: flex;justify-content: center;">BILIBILI</view>
		</view>
		<view v-for="(item,i) in qAndA"></view>
		<view  style="display: flex; flex-direction: row;flex-wrap: wrap;justify-content: space-around;">
			<view class="videos "@click=click(index) v-for="(item,index) in qAndA" :key="index">
				<!--
				<view class="qustion">{{item.question}}</view>
				<view class="author">{{item.answers[0].author}}</view>
				-->
				<image :src="tu(index)" style="width: 100%; height: 80%;"></image>
				<view class="answer">{{item.question.substring(0,20)}}</view>
				<view class="author">{{item.answers[0].author}}</view>
				<!--
				<view class="answer">{{item.answers[0].answer_text.substring(0,20)+'...'}}</view>
				-->
			</view>
			
		</view>
		<view style="width: 100vw; height: 30px;"></view>
		<view class="footer" @click=click02() >
			<view style="display: flex;justify-content: center;">BILIBILI</view>
		</view>
		<!--
				<view class="tabbar">
					<view class="row-container">
						<image v-if="curPage==1" class="icon" @click="clickIcon(1)" src="../../static/zhihu/tabbar/index_blue.svg"></image>
						<image v-else class="icon" @click="clickIcon(1)" src="../../static/zhihu/tabbar/index.svg"></image>
						<text class="text-area">首页1</text>
					</view>
					
					<view class="row-container">
						<image v-if="curPage==2" class="icon" @click="clickIcon(2)" src="../../static/zhihu/tabbar/index_blue.svg"></image>
						<image v-else class="icon" @click="clickIcon(2)" src="../../static/zhihu/tabbar/index.svg"></image>
						<text class="text-area">首页2</text>
					</view>
					
					<view class="row-container">
						<image v-if="curPage==3" class="icon" @click="clickIcon(3)" src="../../static/zhihu/tabbar/index_blue.svg"></image>
						<image v-else class="icon" @click="clickIcon(3)" src="../../static/zhihu/tabbar/index.svg"></image>
						<text class="text-area">首页3</text>
					</view>
				</view>
				-->
		
	</view>

	
</template>

<script>
	import questionAndAnswers from '../../data/zhihu/qa.json'
	export default {
		data() {
			return {
				qAndA:[],
				curPage:1,
			}
		},
		onLoad() {
			console.log(questionAndAnswers)
			this.qAndA = questionAndAnswers
		},
		methods: {
			tu(index){
				index%=8
				return require('./'+index+'.webp')
			},
			click(index){
				console.log(2233)
				uni.navigateTo({
					url: '/pages/bilibili/browser?index='+index
				})
			},
			click02(){
				console.log(2233)
				uni.navigateTo({
					url: '/pages/bilibili/bilibili'
				})
			}
		}
	}
</script>

<style>
	.top{
		width: 100%;
		height: 30px;
		background: #fb7299;
		color: white;
	}
	.footer{
		width: 100%;
		height: 30px;
		background: #fb7299;
		position: fixed;
		bottom: 0;
		color: white;
	}
	.videos{
		display: flex;
		margin: 5px;
		margin-bottom: 10px;
		width: 45vw;
		height: 40vw;
		background: white;
		box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset, rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;

	}
	.a{
		font-size: 10px;
		margin: 0px;
		display: flex;
		justify-content: end;
		
	}
	.fm{
		width: 100%;
		height: 100%;
	}
	.videos{
		display: flex;
		flex-direction: column;
	}
	.tabbar{
			position: fixed;
			bottom: 0;
			display: flex;
			width: 100vw;
			justify-content: space-around;
			height: 10vh;
			background-color: #fb7299;
	}
	.row-container{
				display: flex;
				flex-direction: column;
				justify-content: center;
	}
				
	.icon{
			display: flex;
			width: 15vw;
			height: 15vw;
	}
	
	
	
	
	
	
	
	
.item{
	display: flex;
	width: 170px;
	height: 150px;
	padding: 1vw;
	background-color: aliceblue;
	margin-top: 1vw;
	flex-direction: column;
}
.qustion{
	display: flex;
	font-size: 1vw;
	font-weight: 20;
}
.answer{
	font-size: 1vw;
}
.author{
	font-size: 1vw;
	font-weight: 20;
	display: flex;
}
</style>
