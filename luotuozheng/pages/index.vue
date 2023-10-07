<template>
	<view class="all">
		<view class="zhongjian">
			<view class="wenzi1">小萃</view>
			<view class="wenzi">骆驼证</view>
			<button class="button"hover-class="hover1" @click="tujian">
				<view class="button-text1">图鉴</view>
			</button>
			<button class="button"hover-class="hover1" @click="dianjichouka">
				<view class="button-text1">抽卡</view>
			</button>
		</view>
		<view class="di1">
			<button class="button3"hover-class="hover2" @click="dianji1">
				<view class="button-text1">邀请码</view>
			</button>
			<button class="button4"hover-class="hover2" @click="dianjixjdd">
				<view class="button-text2">新建订单</view>
			</button>
			<button class="button5"hover-class="hover2" @click="dianjimy">
				<view class="button-text">我的订单</view>
			</button>
		</view>
	</view>
</template>
<script>
	export default {
		data() {
			return {
				isClicked: false,
				clicked:false,
			};
		},
		methods: {
			onClick() {
				this.isClicked = !this.isClicked;
			},
			dianji1(){
				this.clicked=true,
				setTimeout(() => {
					uni.navigateTo({
						url:"/pages/yaoqing",
					}),
					this.clicked=false
				}, 500);
			},
			dianjichouka(){
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