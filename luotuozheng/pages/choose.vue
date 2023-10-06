<template>
	<view>
		<view class="zuoshang">
			<image src='/static/hhh/jiantou.png' class="icon" @click="fanhui()"></image>
		</view>
		
		<view class="top">
			
		</view>
	<view class="bigbox">

<!-- 		<view class="zuoshang">
			<image src='/static/hhh/jiantou.png' class="icon" @click="fanhui()"></image>
		</view> -->
		<view class="a">
			
			<view class="titlebox">
				<view class="title">请选择骆驼类型</view>
			</view>
			<view class="b">
				
				<view class="c" @click="drlt()">
					<view class="text">单人骆驼</view>
					<view class="d">
						<image src="../static/骆驼 (2)_00000.png" class="lt_img"></image>
					</view>
				</view>
				<view class="c" @click="qllt()">
					<view class="text">情侣骆驼</view>
					<view class="d">
						<image src="../static/预合成 1_00000.png" class="lt_img"></image>
					</view>
				</view>
			</view>
		</view>
		
		
		
		
		
<!-- 		
		
		<view class="middlebox">
			<text class="text1">单人骆驼</text>
			<text class="text2">情侣骆驼</text>
			<view class="smallbox" @click="drlt()">
				<image src="../static/骆驼 (2)_00000.png" class="image1"></image>
			</view>
			<view class="smallbox" @click="qllt()">
				<image src="../static/预合成 1_00000.png" class="image2"></image>
			</view>
		</view>
		 -->
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
			fanhui(){
				uni.navigateTo({
					url:'/pages/index'
				})
			},
			drlt() {
				// uni.request({
				// 	url: 'http://127.0.0.1:8000/order/create/',
				// 	data: {
				// 		user_id: "114"
				// 	},
				// 	method: "POST",
				// 	success: (res) => {
				// 		console.log(res.data)
				// 		uni.navigateTo({
				// 			url:'/pages/message?order='+res.data.dat
				// 		})
				// 	}
				// })
				uni.navigateTo({
					url:'/pages/message'
				})
			},
			qllt() {
				// uni.request({
				// 	url: 'http://127.0.0.1:8000/order/create/',
				// 	data: {
				// 		user_id: "114"
				// 	},
				// 	method: "POST",
				// 	success: (res) => {
				// 		console.log(res.data)
				// 		uni.navigateTo({
				// 			url:'/pages/message2?order='+res.data.dat
				// 		})
				// 	}
				// })
				uni.navigateTo({
					url:'/pages/message2'
				})
			},
		},
	};
</script>

<style>
	.bigbox{
		display: flex;
		justify-content: center;
		margin-top: 30px;
	}
	.zuoshang {
		position: fixed;
		margin-top: 1vh;
		margin-left: 1vh;
	}
	.icon {
		height: 4vh;
		width: 4vh;
		display: flex;
		justify-content: flex-start;
	}
	.a{
		
		width: 90vw;
		height: 100vw;	
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.b{
		margin-top: 40px;
		display: flex;
		flex-direction: row;
		align-items: center;
	}
	.c{
		text-align: center;
		width: 45vw;
		height: auto;
	}
	
	.lt_img{
		width: 42vw;
		height: 35vw;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
	}
	.text{
		margin-top: 10rpx;
		margin-bottom: 10rpx;
		font-size: 50rpx;
	}
	.titlebox{
		margin-top: 40rpx;
	}
	.title{
		font-size: 60rpx;
	}


	.top {
		
		width: 100vw;
		height: 6vh;
		background: linear-gradient(to bottom, #FF6E53, #FF6E52, #FF8453 40%, #FF9758, #FFA859);
		/* z-index: -2; */
	}
</style>