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
		<view class="item" v-for="(item,index) in vids" :key="index" @click="openItem(index)">
			<div class="thumbnail_wrapper">
				<image :src="item.thumbnail" mode="aspectFill"></image>
			</div>
			<view class="question">{{clampText(item.question, 9)}}</view>
			<view class="author">{{item.answers[0].author}}</view>
		</view>
	</view>
</template>

<script>
	
	import questionAndAnswers from 'data/zhihu/qa.json'
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
	width: 44vw;
	padding: 0;
	margin: 1vw;
	height: 50vw;
	padding: 1vw;
	background-color: #fafafa;
	margin-top: 1vw;
	flex-direction: column;
	border-radius: 2vw;
	border: 0.3vw;
	border-style:solid;
	border-color: #f0f0f0;
}
.question{
	display: flex;
	font-size: 4vw;
	font-weight: 20;
}
.author{
	font-size:3vw;
	font-weight: 10;
}
</style>
