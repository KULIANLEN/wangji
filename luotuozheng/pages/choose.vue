<template>
	<view class="bigbox">
		<view class="top">

		</view>
		<view class="titlebox">
			<text class="title">请选择</text><br>
			<text class="title2">要创建的骆驼种类</text>
		</view>
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
		<view class="backgroundcolor">

		</view>
		<view class="decoration">
			<image src="../static/yezi1.png" class="bottom1"></image>
			<image src="../static/yezi2.png" class="bottom2"></image>
			<image src="../static/yezi2.png" class="bottom3"></image>
			<image src="../static/flower1.png" class="bottom4"></image>
			<image src="../static/flower2.png" class="bottom5"></image>
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
			dl() {
				uni.request({
					url: 'http://127.0.0.1:8001/app/login',
					data: {
						n1: this.username,
						n2: this.password
					},
					method: "GET",
					success: (res) => {
						console.log(res.data.code)
						this.msg = res.data.code
						if (this.msg == "登录成功") {
							uni.navigateTo({
								url: '/pages/tu/tu'
							})
						}
					}
				})
			},
			drlt() {
				console.log("drlt")

				uni.request({
					url: 'http://127.0.0.1:8000/order/create/',
					data: {
						user_id: "114"
					},
					method: "POST",
					success: (res) => {
						console.log(res.data)
						uni.navigateTo({
							url:'/pages/message'
						})
					}
				})
			},
			qllt() {
				console("qllt")
				uni.request({
					url: 'http://127.0.0.1:8000/order/create/',
					data: {
						user_id: "114"
					},
					method: "POST",
					success: (res) => {
						console.log(res.data)
						uni.navigateTo({
							url:'/pages/message2'
						})
					}
				})
			},
		},
	};
</script>

<style>
	.bottom1 {
		position: absolute;
		bottom: 20%;
		left: 0%;
		margin-left: -10vw;
		width: 30vw;
		height: 30vw;
	}

	.bottom2 {
		width: 30vw;
		height: 30vw;
		position: absolute;
		bottom: 0%;
		left: -10%;
	}

	.bottom3 {
		width: 30vw;
		height: 30vw;
		position: absolute;
		bottom: 0%;
		left: -5%;
		/* z-index: -1; */
	}

	.bottom4 {
		width: 50vw;
		height: 30vw;
		position: absolute;
		bottom: 0%;
		right: -20%;
		/* z-index: 0; */

	}

	.bottom5 {
		width: 20vw;
		height: 20vw;
		position: absolute;
		top: 20%;
		right: -5%;
	}

	.text1 {
		position: absolute;
		top: 40%;
		font-size: 8vw;
		left: 8vw;
	}

	.text2 {
		position: absolute;
		top: 40%;
		font-size: 8vw;
		left: 59vw;
	}

	.image2 {
		width: 42vw;
		height: 30vw;
		margin-top: 10vw;
		margin-left: 2vw;
	}

	.image1 {
		width: 30vw;
		height: 25vw;
		margin-top: 10vw;
		margin-left: 6vw;
	}

	.smallbox {
		width: 45vw;
		height: 45vw;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);

	}

	.bigbox {
		display: flex;
		align-items: center;
		flex-direction: column;
		/* z-index: -10; */
	}

	.middlebox {
		width: 94vw;
		height: 120vw;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
		margin-top: 5vw;
		display: flex;
		justify-content: space-between;
		align-items: center;
		background-color: rgba(255, 255, 255, 0.9);
		/* z-index: -1; */

	}

	.top {
		position: absolute;


		width: 100vw;
		height: 6vh;
		background: linear-gradient(to bottom, #FF6E53, #FF6E52, #FF8453 40%, #FF9758, #FFA859);
		/* z-index: -2; */
	}

	.backgroundcolor {
		width: 100vw;
		height: 100vh;
		z-index: -10;
		background-color: #f5f5f5;
		position: absolute;
		top: 0%;
	}

	.titlebox {
		margin-top: 10vw;

	}

	.title2 {
		margin-left: -20vw;
		font-size: 8vw;
	}

	.title {
		margin-left: -20vw;
		text-align: center;
		font-size: 15vw;
	}
</style>