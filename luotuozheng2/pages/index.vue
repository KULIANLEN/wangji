<template>
	<view class="all">
		<!-- <view class="image">
			<image src="road.png" class="image"></image>
		</view> -->
		<view class="top">
			<view class="qrcode" @click="click01()">二维码</view>
			<!-- <view class="tj" @click="click02()"></view> -->
		</view>
		<view class="bigbox">
			<view class="box1" @click="click03()">新建订单</view>
			<view class="box2" @click="click04()">我的订单</view>
			<view class="box3" @click="click05()">去抽卡</view>
			
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			};
		},
		methods: {
			click01(){
				console.log(2233)
				uni.navigateTo({
					url: '/pages/qrcode'
				})
			},
			click02(){
				console.log(2233)
				uni.navigateTo({
					url: '/pages/detail'
				})
			},
			click03(){
				console.log(2233)
				uni.navigateTo({
					url: '/pages/detail'
				})
			},
			click04(){
				console.log(2233)
				uni.navigateTo({
					url: '/pages/list'
				})
			},
			click05(){
				console.log(2233)
				uni.navigateTo({
					url: '/pages/chouka'
				})
			},
		},
	};
</script>

<style>
	.image{
		width: 10vw;
		height: 10vh;
		z-index: -5; 
		 margin-top: -100vw;
		
		
	}
	.all{
		/* display: flex; */
		width: 100vw;
		/* flex-direction: column; */
	}
	.top{
		background: linear-gradient(to   right,#FF6E53 0 , #FF6E52 , #FF8453  , #FF9758  ,#FFA859 100% );
		width: 100vw;
		height: 9vh;
		display: flex;
		justify-content: space-around;
		align-items: center;
		font-size: 20px;
		color: aliceblue;
	}
	.qrcode{
		width: 30px;
		height: 30px;
		background: white;
	}
	.tj{
		width: 30px;
		height: 30px;
		background: white;
	}
	.bigbox{
		display: flex;
		justify-content: space-between;
		align-items: center;
		height: 81vh;
	}
	.box1{
		width: 60px;
		height: 60px;
		background: linear-gradient(to   right,#FF6E53 0 , #FF6E52 , #FF8453  , #FF9758  ,#FFA859 100% );
	}
	.box2{
		width: 60px;
		height: 60px;
		background: linear-gradient(to   right,#FF6E53 0 , #FF6E52 , #FF8453  , #FF9758  ,#FFA859 100% );
	}
	.box3{
		width: 60px;
		height: 60px;
		background: linear-gradient(to   right,#FF6E53 0 , #FF6E52 , #FF8453  , #FF9758  ,#FFA859 100% );
	}
	
	
	
	
	
	
	
	
	
</style>