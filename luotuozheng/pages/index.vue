<template>
	<view style="position: relative;">
		<image class="background-img" src="../static/images/index_img/bg.png" mode="widthFix"></image>
		<image class="create-button" @click="clickCreateCamel" src="../static/images/index_img/create_button.svg"
			mode="widthFix"></image>
		<image class="myCamel-button" @click="ClickMyCamel" src="../static/images/index_img/myCamel_button.svg"
			mode="widthFix"></image>
	</view>
	<!-- 	<view class="all">
		<view class="top">
			<view class="wenzi">小萃骆驼证</view>
			<view class="button_gongyou button1" @click="tujian">
				<view class="button-text text0">图鉴</view>
			</view>
			<view class="button_gongyou button2" @click="clickCreateCamel">
				<view class="button-text text0">抽卡</view>
			</view>
		</view>
		<view class="main">
			<view class='main_gonyou'></view>
			<view class="main_gongyou button3" @click="dianjiyqm">
				<view class="button-text text1">邀请码</view>
			</view>
			<view class="main_gongyou button4" @click="dianjixjdd">
				<view class="button-text text2">新建订单</view>
			</view>
			<view class="main_gongyou button5" @click="dianjimy">
				<view class="button-text text3">我的订单</view>
			</view>
		</view>
		<image class='dibiao1' src='/static/homepage_dibiao.png'></image>
		<image class='dibiao2' src='/static/homepage_dibiao.png'></image>
		<image class='dibiao3' src='/static/homepage_dibiao.png'></image>
	</view> -->
</template>
<script>
	export default {
		data() {
			return {
				clicked: false,
				orderId: 0,
			};
		},
		methods: {
			
			ClickMyCamel() {
				this.clicked = true,
					// setTimeout(() => {
					uni.navigateTo({
						url: "/pages/list",
					}),
					this.clicked = false
				// }, 0);
			},

			clickCreateCamel() {
				var that = this
				uni.showToast({
					icon: "loading",
					title: "创建中...",
				})
				uni.request({
					url: 'http://127.0.0.1:8000/user/create/',
					data: {
						user_id: getApp().globalData.userId,
					},
					fail(res) {
						console.log(res)
						uni.hideToast()
						uni.showToast({
							icon: "error",
							title: "服务器连接失败",
						})
					}
				})
				uni.request({
					url: 'http://127.0.0.1:8000/order/create/',
					data: {
						user_id: getApp().globalData.userId,
					},
					method: "POST",
					success: (res) => {
						if (res.data.code == 1) {
							uni.hideToast()
							setTimeout(() => {
								uni.navigateTo({
									url: "/pages/diyzhuangban?order=" + res.data.dat +
										"&mode=create",
								})
							}, 300);
						} else {
							console.log()
							uni.showToast({
								icon: "error",
								title: "创建失败" + res.data.msg,
							})
							// setTimeout(() => {
							// 	uni.hideToast()
							// }, 750);
						}
					}
				})
			},
			// dianjiyqm() {
			// 	this.clicked = true,
			// 		setTimeout(() => {
			// 			uni.navigateTo({
			// 					url: "/pages/yaoqing",
			// 				}),
			// 				this.clicked = false
			// 		}, 500);
			// },
			// chouka() {
			// 	this.clicked = true,
			// 		setTimeout(() => {
			// 			uni.navigateTo({
			// 					url: "/pages/chouka",
			// 				}),
			// 				this.clicked = false
			// 		}, 500);
			// },
			// dianjixjdd() {
			// 	this.clicked = true;
			// 	setTimeout(() => {
			// 		uni.navigateTo({
			// 				url: "/pages/choose",
			// 			}),
			// 			this.clicked = false
			// 	}, 500);
			// },
			// tujian() {
			// 	this.clicked = true,
			// 		setTimeout(() => {
			// 			uni.navigateTo({
			// 					url: "/pages/tujian",
			// 				}),
			// 				this.clicked = false
			// 		}, 500);
			// },
		},
		

	};
</script>
<style>
	.background-img {
		width: 100vw;
		z-index: 0;
	}

	.create-button {
		width: 50vw;
		z-index: 5;
		position: absolute;
		left: 8vw;
		margin-top: 80vw;
		box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset, rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
	}

	.myCamel-button {
		width: 50vw;
		z-index: 5;
		position: absolute;
		left: 8vw;
		margin-top: 120vw;
		box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset, rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
	}

	/* @import '/style/index.css'; */
</style>