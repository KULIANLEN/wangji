<template>
	<view>
		
		
		<view class="content">
			<view class="text-area">
				<text class="title">{{title}}</text>
			</view>
		</view>
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
	</view>
</template>

<script>
	export default {
		data() {
			return {/*
				title: '45454',
				width:45,
				curPage:0,*/
			}
		},
		onLoad() {
			console.log("onLoad")
		},
		onShow() {
			console.log("onShow")
		},
		methods: {
			clickIcon(index){
				console.log(index)
				this.curPage = index
			}
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 80vh
	}
	.tabbar{
		display: flex;
		justify-content: space-around;
		height: 10vh;
		background-color: #8f8f94;
	}
	.icon{
		display: flex;
		width: 15vw;
		height: 15vw;
	}
	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
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
</style>
