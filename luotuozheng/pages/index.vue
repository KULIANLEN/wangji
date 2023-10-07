<template>
	<view class="all">
		<view class="top">
			<view class="wenzi_gongyou wenzi1">小萃</view>
			<view class="wenzi_gongyou wenzi2">骆驼证</view>
			<button class="button_gongyou button1" @click="tujian">
				<view class="button-text text0">图鉴</view>
			</button>
			<button class="button_gongyou button2"@click="chouka">
				<view class="button-text text0">抽卡</view>
			</button>
		</view>
		<view class="main">
			<button class="button_gongyou button3" @click="dianjiyqm">
				<view class="button-text text1">邀请码</view>
			</button>
			<button class="button_gongyou button4" @click="dianjixjdd">
				<view class="button-text text2">新建订单</view>
			</button>
			<button class="button_gongyou button5" @click="dianjimy">
				<view class="button-text text3">我的订单</view>
			</button>
		</view>
	</view>
</template>
<script>
	export default {
		data() {
			return {
				clicked:false,
			};
		},
		methods: {
			dianjiyqm(){
				this.clicked=true,
				setTimeout(() => {
					uni.navigateTo({
						url:"/pages/yaoqing",
					}),
					this.clicked=false
				}, 500);
			},
			chouka(){
				this.clicked=true,
				setTimeout(() => {
					uni.navigateTo({
						url:"/pages/chouka",
					}),
					this.clicked=false
				}, 500);
			},
			dianjixjdd(){
				this.clicked=true,
				setTimeout(() => {
					uni.navigateTo({
						url:"/pages/choose",
					}),
					this.clicked=false
				}, 500);
			},
			dianjimy(){
				this.clicked=true,
				setTimeout(() => {
					uni.navigateTo({
						url:"/pages/list",
					}),
					this.clicked=false
				}, 500);
			},
			tujian(){
				this.clicked=true,
				setTimeout(() => {
					uni.navigateTo({
						url:"/pages/tujian",
					}),
					this.clicked=false
				}, 500);
			}
		}
	};
</script>
<style>
	@import '/style/index.css';
</style>