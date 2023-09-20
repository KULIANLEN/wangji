<template>
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
						<view class="txt">{{el.single ? "单身驼" : "情侣驼"}}</view>
						<view class="txt">{{"订单编号："+el.orderId}}</view>
					</view>
					<view class="b2">
						<view class="status" :style="'color:'+mapStatus2Color(el.status)+';'">{{mapStatus2Txt(el.status)}}</view>
					</view>
				</view>
			</view>
			
		</view>
		<view class="footer"></view>
	</view>
</template>

<script>
	var _self;
	export default {
		data() {
			return {
				user_id: '114',
				username: '',
				password: '',
				code:'',
				msg:"",
				orders: [],
			};
		},
		onShow(){
			uni.request({
				url:'http://127.0.0.1:8000/user/query/'+ this.user_id +'/?query=orders.{id|extra|status|complement.{owner.id|extra.name}}',
				method:"GET",
				success : (res)=>{
					this.orders = [];
					res.data.dat.orders.forEach((e)=>{
						this.orders.push({
							orderId : e.id,
							camelName : e.extra.name + (e.complement === null ? '' : ' & ' + e.complement.extra.name),
							single : e.complement === null,
							status : e.status,
						});	
					})
					console.log(this.orders);
				}
			})
		},
		methods: {
			dl() {
				uni.request({
					url:'http://127.0.0.1:8001/app/login',
					data:{
						n1:this.username,
						n2:this.password
					},
					method:"GET",
					success:(res)=>{
						console.log(res.data.code)
						this.msg=res.data.code
						if(this.msg=="登录成功"){
							uni.navigateTo({
								url: '/pages/tu/tu'
							})
						}
					}
				})
			},
			xx(){
				this.msg="66666"
			},
			click03(){
				console.log(2233)
				uni.navigateTo({
					url: '/pages/signup/signup'
				})
			},
			ddxq(){
				uni.navigateTo({
					url: '/pages/diyzhuangban'
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
					return "#FF0000";
					case 1:
					return "#dddd00";
					case 2:
					return "#00FF00";
				}
			},
			redirect2OrderDetail(idx){
				uni.navigateTo({
					url: '/pages/diyzhuangban?order='+this.orders[idx].orderId
				})
			}
		},
	};
</script>

<style>
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
	}
	.dd{
		height: 125px;
		width: auto;
		background: white;
		margin-left: 10px;
		margin-right: 10px;
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