<template>
	<view class="aa">
		<view class="v"></view>
		<!--
		<view>
			<image src="./1.wepb" style="width: 100px; height: 100px;"></image>
		</view>
		-->
		<view class="bb">
			<view class="qustion">{{qestionAndAnswer[showingIndex].question}}</view>
		</view>
		<view class="cc">
			<view v-if="xxx==1" class="c1" style="background: white;color:black" @click="click01(1)">简介</view>
			<view v-else class="c1" style="background: #fb7299;color:white" @click="click01(1)">简介</view>
			<view v-if="xxx==2" class="c1" style="background: white;color:black" @click="click01(2)">评论</view>
			<view v-else class="c1" style="background: #fb7299;color:white" @click="click01(2)">评论</view>
		</view>
		<view v-if="xxx==1" class="jj">
			<view class="dd">{{qa[showingIndex].question}}</view>
		</view>
		<view v-else="xxx==2" class="pl">
			<view class="ee" v-for="(t,i) in qa[showingIndex].answers">
				<view style="font-size: 18px;">{{t.author}}</view>
				<view style="font-size: 10px;">{{t.answer_text}}</view>
			</view>
		</view>
		<view style="width: 100vw; height: 30px;"></view>
		<view class="footer" @click=click02() >
			<view style="display: flex;justify-content: center;">返回主页</view>
		</view>
		
		<!--
			<view>
				<image :src="tu(index)" style="width: 100%; height: 80%;"></image>
			</view>
			-->
	</view>

</template>

<script>
	import qa from '../../data/zhihu/qa.json'
	export default {
		data() {
			return {
				qestionAndAnswer:[],
				showingIndex:0,
				xxx:1,
				qa:[],
				urlurl:"./0.webp",
			}
		},
		
		onLoad() {
			this.qa=qa
		},
		onShow() {
			this.qestionAndAnswer = qa
			console.log(this.qestionAndAnswer)
			this.showingIndex = this.$route.query.index;
			if(!this.showingIndex) this.showingIndex=0
			console.log(this.showingIndex)
		},
		methods: {
			click01(index){
				console.log(index)
				this.xxx = index
			},
			tu(index){
				index%=8
				return require('./'+index+'.webp')
			},
			click02(){
				console.log(2233)
				uni.navigateTo({
					url: '/pages/bilibili/bilibili'
				})
			},
		}
	}
</script>

<style>
	.v{
		width: 100vw;
		height:50vw;
		display: flex;
		
		background-image: url("./0.webp");
		
		background-repeat: no-repeat;
        background-size: 100% 100%;
	}
	.aa{
		display: flex;
		flex-direction: column;
	}
	.bb{
		width: 100vw;
		height: 24px;
	}
	.cc{
		display: flex;
		background: #fb7299;
		width: 100vw;
		height: 24px;
		border: solid #fb7299  1px;
	}
	.c1{
		height: 100%;
		width: 100px;
		text-align: center;
		background: white;
	}
	.ee{
		margin-bottom: 10px;
	}
	.qustion{
		display: flex;
		
	}
	.jj{
		width: 100vw;
		height: 100px;
	}
	.pl{
		width: 100vw;
		height: 100px;
	}
	.footer{
		width: 100%;
		height: 30px;
		background: #fb7299;
		position: fixed;
		bottom: 0;
		color: white;
	}
</style>
