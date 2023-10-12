<template>
	<view style="position: relative;">
		<image class="background-img" src="../static/images/index_img/bg.png" mode="widthFix"></image>
		<image class="create-button" @click="clickCreateCamel" src="../static/images/index_img/create_button.svg"
			mode="widthFix"></image>
		<image class="myCamel-button" @click="ClickMyCamel" src="../static/images/index_img/myCamel_button.svg"
			mode="widthFix"></image>
	</view>
</template>
<script>
	export default {
		data() {
			return {
				orderId: 0,
			};
		},
		methods: {
			
			ClickMyCamel() {
				uni.navigateTo({
					url: "/pages/list",
				})
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
						}
					}
				})
			},
			
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
</style>