<template>
	<view class="all">
		<view class="top">
			<view class="wenzi">小萃骆驼证</view>
			<view class="button_gongyou button1" @click="tujian">
				<view class="button-text text0">图鉴</view>
			</view>
			<view class="button_gongyou button2"@click="chouka">
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