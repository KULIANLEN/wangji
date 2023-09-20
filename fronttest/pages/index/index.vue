<template>
	<view class="content">
		<image class="logo" src="/static/logo.png"></image>
		<view class="text-area">
			<text class="title">{{title}}</text>
		</view>
		<view style="display: flex;flex-direction: column;">
			<view style="background-color: aqua;">
				<input v-model="a"  placeholder="输入数字a">
				<view style="background-color: aliceblue;height: 20rpx;"></view>
				<input v-model="b" placeholder="输入数字b">
			</view>
			<button @click="calc"> submit</button>
			
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: 'Hello',
				a :'',
				b : ''
			}
		},
		onLoad() {

		},
		methods: {
			calc(){
				uni.request({
					url:'http://localhost:8000/app/add',
					method:'GET',
					data:{
						num1:this.a,
						num2:this.b
					},
					success: (res) => {
						this.title = res.data.res
					}
				})
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
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
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
