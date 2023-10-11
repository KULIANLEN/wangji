<template>
	<view>
	<view class="zuoshang">
		<image src='/static/hhh/jiantou.png' class="icon" @click="fanhui()"></image>
	</view>
	<view class="all">
		<view class="top">
			<view>我的订单</view>
		</view>
		<view class="ddlist">
			<view class="dd" 
			v-for="(el, idx) in orders"
			:key="idx"
			@click="redirect2OrderDetail(idx)">
				<view class="a1">
					<view class="lt_name">{{el.camelName}}</view>
				</view>
				<view class="a2">
					<view class="b1">
						<view class="txt">年龄：{{el.lt_age}}岁</view>
						<view class="txt">体型：{{el.lt_body}}</view>
						<view class="txt">{{"订单编号："+el.orderId}}</view>
					</view>
					<view class="b2">
						<view class="status" :style="'color:'+mapStatus2Color(el.status)+';'">{{mapStatus2Txt(el.status)}}</view>
					</view>
				</view>
			</view>
			
		</view>
		<view class="footer"></view>
	</view></view>
</template>

<script>
	var _self;
	export default {
		data() {
			return {
				username: '',
				password: '',
				code:'',
				msg:"",
				orders: [],
			};
		},
		onShow(){
			uni.request({
				url:'http://127.0.0.1:8000/user/query/'+ getApp().globalData.userId +'/?query=orders.{id|extra|status|complement.{owner.id|extra.name}}',
				method:"GET",
				success : (res)=>{
					this.orders = [];
					res.data.dat.orders.forEach((e)=>{
						this.orders.push({
							orderId : e.id,
							camelName : e.extra.name + (e.complement === null ? '' : ' & ' + e.complement.extra.name),
							lt_food : e.extra.lt_food,
							//single : lt_zt=="1"?"单身":(lt_zt=="2"?"恋爱中":(lt_zt=="3"?"其它":"未知")),
							status : e.status,
							lt_age : e.extra.lt_age,
							lt_body: e.extra.lt_body=="1"?"胖":(e.extra.lt_body=="2"?"微胖":(e.extra.lt_body=="3"?"瘦":(e.extra.lt_body=="4"?"很瘦":"未知"))),
						});	
					})
				}
			})
		},
		methods: {
			xx(){
				this.msg="66666"
			},
			click03(){
				console.log(2233)
				uni.navigateTo({
					url: '/pages/signup/signup'
				})
			},
			mapStatus2Txt(status){
				switch(status){
					case 0:
					return "未提交";
					case 1:
					return "等待配对";
					case 2:
					return "已提交";
				}
			},
			mapStatus2Color(status){
				switch(status){
					case 0:
					return "rgb(253, 118, 91)";
					case 1:
					return "#dddd00";
					case 2:
					return "rgb(42, 111, 42)";
				}
			},
			
			redirect2OrderDetail(idx){
				uni.navigateTo({
					url: '/pages/detail?order='+this.orders[idx].orderId+'&status='+this.orders[idx].status
				})
			},
			
			// redirect2OrderDetail(idx){
			// 	uni.navigateTo({
			// 		url: '/pages/diyzhuangban?order='+this.orders[idx].orderId
			// 	})
			// },
			
			fanhui(){
				uni.navigateTo({
					url:'/pages/index'
				})
			}
		},
	};
</script>

<style>
	.zuoshang {
		position: fixed;
		margin-top: 36rpx;
		margin-left: 15rpx;
	}
	.icon {
		height: 4vh;
		width: 4vh;
		display: flex;
		justify-content: flex-start;
	}
	.all{
		display: flex;
		width: 100vw;
		flex-direction: column;
	}
	.top{
		background: linear-gradient(to   right,#FF6E53 0 , #FF6E52 , #FF8453  , #FF9758  ,#FFA859 100% );
		width: 100vw;
		height: 160px;
		display: flex;
		justify-content: center;
		/* align-items: center; */
		font-size: 20px;
		color: aliceblue;
		z-index: -3;
	}
	.ddlist{
		margin-top: -110px;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		
	}
	.dd{
		height: 140px;
		width: 90vw;
		background: white;
/* 		margin-left: 10px;
		margin-right: 10px; */
		margin-top: 15px;
		border-radius: 10px;
		box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset, rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
	}
	.a1{
		height: 30%;
		display: flex;
		align-items: center;
		padding: 2px;
		border-radius: 10px 10px 0 0;
		background: rgb(251, 242, 232);
		/* background: rgb(255, 213, 161); */

	}
	.lt_name{
		margin-left: 5px;
	}
	.a2{
		height: 70%;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	}
	.b1{
		font-size: 12px;
		height: 100%;
		display: flex;
		flex-direction: column;
		margin-top: 7px;
	}
	.b2{
		display: flex;
		height: 100%;
		align-items: center;
		margin-right: 30px;
	}
	.txt{
		margin-top: 5px;
		margin-bottom: 5px;
		margin-left: 6px;
		color: rgb(67, 67, 67);
	}
	.status{
		color: rgb(42, 111, 42);
	}
	.and{
		color: hotpink;
		font-weight: bold;
		margin-left: 5px;
		margin-right: 5px;
	}
</style>