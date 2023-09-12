<template>
	<view class="container">
		
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
		
		<view class="item" v-for="(item,index) in vids">
			<div class="thumbnail_wrapper">
				<image :src="item.thumbnail" mode="widthFix"></image>
			</div>
			<view class="qustion">{{item.question}}</view>
			<view class="author">{{item.answers[0].author}}</view>
		</view>
		<view class="bottom_nav">
			<image @click="selectedBottomElem=0" v-if="selectedBottomElem!=0" src="../../static/zhihu/tabbar/about.png"></image>
			<image v-else src="../../static/zhihu/tabbar/about_cur.png"></image>
			<image @click="selectedBottomElem=1" v-if="selectedBottomElem!=1" src="../../static/zhihu/tabbar/plugin.png"></image>
			<image v-else src="../../static/zhihu/tabbar/plugin_cur.png"></image>
			<image @click="selectedBottomElem=2" v-if="selectedBottomElem!=2" src="../../static/zhihu/tabbar/component.png"></image>
			<image v-else src="../../static/zhihu/tabbar/component_cur.png"></image>
			<image @click="selectedBottomElem=3" v-if="selectedBottomElem!=3" src="../../static/zhihu/tabbar/basics.png"></image>
			<image v-else src="../../static/zhihu/tabbar/basics_cur.png"></image>
		</view>
	</view>
</template>

<script>
	import questionAndAnswers from '../../data/zhihu/qa.json'
	export default {
		data() {
			return {
				vids:[],
				selectedBottomElem:0
			}
		},
		onLoad() {
			
		},
		onShow() {
			var thumbnail_count = 8;
			this.vids = questionAndAnswers;
			for(var e of this.vids){
				var t_idx = Math.floor(Math.random() * thumbnail_count);
				e.thumbnail = "/static/imgs/thumbnails/"+t_idx+".jpg";
				if(e.question.length > 10)
					e.question = e.question.substr(0, 10)+"...";
			}
		},
		methods: {
			
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
.qustion{
	display: flex;
	font-size: 4vw;
	font-weight: 20;
}
.bottom_nav{
	width: 100%;
	height: 5vh;
	background-color: pink;
	bottom: 0;
	position: fixed;
	display: flex;
	justify-content: space-around;
	align-items: center;
}
.bottom_nav image{
	height:10vw;
	width: 10vw;
}
</style>
