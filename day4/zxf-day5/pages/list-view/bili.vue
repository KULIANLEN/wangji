<template>
	<view class="container">
		<!--
		<swiper class="swiper" circular :indicator-dots="indicatorDots" :autoplay="autoplay" :interval="interval" :duration="duration">
			<swiper-item>
				<view class="1">1</view>
			</swiper-item>
			<swiper-item>
				<view class="2">2</view>
			</swiper-item>
			<swiper-item>
				<view class="3">3</view>
			</swiper-item>
		</swiper>
		-->
		<view class="item" v-for="(item,index) in vids" @click="openItem(index)">
			<div class="thumbnail_wrapper">
				<image :src="item.thumbnail" mode="widthFix"></image>
			</div>
			<view class="question">{{clampText(item.question, 9)}}</view>
			<view class="author">{{item.answers[0].author}}</view>
		</view>
	</view>
</template>

<script>
	
	import questionAndAnswers from 'data/zhihu/qa.json'
	var a = {e1:"asdasd", ease:121212};
	function f(){
		a.e1 = 123;
		a = {
			a1:"asdasd", 
			kga:121213,
			afunc(){
				var x = 1;

			}
		};
	}
	export default {
		data() {
			return {
				vids:[],
				selectedBottomElem:0
			}
		},
		onLoad() {
			
		},
		created(){
			var thumbnail_count = 8;
			this.vids = questionAndAnswers;
			for(var e of this.vids){
				var t_idx = Math.floor(Math.random() * thumbnail_count);
				e.thumbnail = "/static/imgs/thumbnails/"+t_idx+".jpg";
				
			}
		},
		onShow() {
			
		},
		methods: {
			openItem(idx){
				console.log('/pages/basics/browse?idx='+idx);
				uni.navigateTo({
					url: '/pages/basics/browse?idx='+idx
				});
			},
			clampText(text, length){
				if(text.length > length)
					text = text.substr(0, length)+"...";
				return text;
			}
		}
	}
</script>

<style>
	
	.thumbnail_wrapper{
		width:100%;
		height:80%;
		overflow: hidden;
	}
.container{
	display: flex;
	flex-direction: row;
	flex-wrap: wrap;
	justify-content: center;
	margin:0;
	padding: 0;
}
.item{
	display: flex;
	width: 45%;
	padding: 0;
	margin: 1%;
	height: 50vw;
	padding: 1vw;
	background-color: aliceblue;
	margin-top: 1vw;
	flex-direction: column;
}
.qeustion{
	display: flex;
	font-size: 4vw;
	font-weight: 20;
}
</style>
