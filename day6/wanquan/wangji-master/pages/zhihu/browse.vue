<template>
	<view>
		<image class='picture' :src="convert(showingIndex)"></image>
		<!-- <view class="jianjie2">简介 评论</view> -->
		<image class="jianjie" src="../../static/image/jianjie.png"></image>
		
		
		<!-- <image class="yjsl" src="../../static/image/img11.png"></image> -->
		<swiper class='swip'>
			<swiper-item class="jianjieswi">
				<view class="author">{{qestionAndAnswer[showingIndex].answers[0].author}}</view>
				<view class="qustion">{{qestionAndAnswer[showingIndex].question}}</view>
				<view class="yjsl2">
					<image v-if="curdianzan==1" class="picjysl1" @click="clickdianzan()" src="/static/image/weidianzan.png" mode="aspectFit"></image>
					<image v-else class="picjysl2" @click="clickdianzan()" src="/static/image/yidianzan.png" mode="aspectFit"></image>
					<image class="picjysl1" src="/static/image/weibuxihuan.png" mode="aspectFit"></image>
					<image v-if="curtoubi==1" class="picjysl1" @click="clicktoubi()" src="/static/image/weitoubi.png" mode="aspectFit"></image>
					<image v-else class="picjysl2" @click="clicktoubi()" src="/static/image/yitoubi.png" mode="aspectFit"></image>
					<image v-if="curshoucang==1" class="picjysl1" @click="clickshoucang()" src="/static/image/weishoucang.png" mode="aspectFit"></image>
					<image v-else class="picjysl2" @click="clickshoucang()" src="/static/image/yishoucang.png" mode="aspectFit"></image>
					<image v-if="curfenxiang==1" class="picjysl1" @click="clickfenxiang()" src="/static/image/weizhuanfa.png" mode="aspectFit"></image>
					<image v-else class="picjysl2" @click="clickfenxiang()" src="/static/image/yizhuanfa.png" mode="aspectFit"></image>
				
				</view>
				<view>
					<image class="guanggao" src="../../static/image/guanggao.png"></image>
				</view>
				
			</swiper-item>
			
			<swiper-item class="pinglunswi">
				<image class='pinglunshangduan' src="/static/image/pinglunshangduan.png"></image>
				<view class="pinglun" v-for="(item,index) in qestionAndAnswer[showingIndex].answers" :key="index">
					<view class="detail1">{{item.author}}</view>
					<br>
					<view class="detail2">{{item.answer_text}}</view>
				</view>
				<image class='pinglunxiaduan' src="/static/image/pinglunxiaduan.png"></image>
			</swiper-item>
		</swiper>
		
		<!-- <image class="guanggao" src="../../static/image/guanggao.png"></image> -->
		
		
	</view>
</template>

<script>
	import qa from '../../data/zhihu/qa.json'
	export default {
		data() {
			return {
				qestionAndAnswer:[],
				showingIndex:0,
				curdianzan:false,
				curtoubi:false,
				curshoucang:false,
				curfenxiang:false,
			}
		},
		
		onLoad() {
			
		},
		onShow() {
			this.qestionAndAnswer = qa
			console.log(this.qestionAndAnswer)
			this.showingIndex = this.$route.query.index;
			if(!this.showingIndex) this.showingIndex=0
			console.log(this.showingIndex)
		},
		methods: {
			clickdianzan(){
				if(this.curdianzan==0)this.curdianzan=1;
				else this.curdianzan=0;
			},
			clicktoubi(){
				if(this.curtoubi==0)this.curtoubi=1;
				else this.curtoubi=0;
			},
			clickshoucang(){
				if(this.curshoucang==0)this.curshoucang=1;
				else this.curshoucang=0;
			},
			clickfenxiang(){
				if(this.curfenxiang==0)this.curfenxiang=1;
				else this.curfenxiang=0;
			},
			convert(index){
				index = index%4+1
				return require('../../static/image/img'+ index +'.png')
			},
		}
	}
</script>

<style>
	.pinglunxiaduan{
		width:100vw;
		height:45px;
	}
	.pinglunshangduan{
		width:100vw;
		height:45px;
	}
	.detail1{
		font-family:'楷体';
		font-weight: 100;
		font-size: 15px;
	}
	.detail2{
		font-family: '楷体';
		font-weight: 600;
		font-size: 15px;
	}
	.swip{
		height:100vh;
	}
	.pinglun{
		/* background-color: aliceblue; */
		padding-left:20px;
		padding-right:6px;
		border-bottom: 1px solid #ddd;
	}
	.pinglunswi{
		flex-wrap: wrap;
		height:100vh;
	}
	.jianjieswi{
		height:1000px;
	}
	.yjsl2{
		display:flex;
		justify-content: space-between;
		width:100vw;
	}
	.picjysl1{
		display:flex;
		width: 90px;
		height:90px;
	}
	.picjysl2{
		display:flex;
		width: 85px;
		height:85px;
	}
	.jianjie2{
		font-family:'楷体'
	}
	.author{
		margin-left:5px;
	}
	.picture{
		width: 100vw;
		height: 53vw;
	}
	.yjsl{
		display: flex;
		width:100vw;
		height: 90px;
	}
	.guanggao{
		display: flex;
		width:100vw;
		height:330px;
	}
	.jianjie{
		width:100vw;
		height:35px;
	}
</style>
