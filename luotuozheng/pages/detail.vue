<template>
	<view>
		<view class="zuoshang">
			<image src='/static/hhh/jiantou.png' class="icon" @click="fanhui()"></image>
		</view>
		<view class="all">

			<view class="top">
				<view>订单详情</view>
			</view>

			<view class="box1">
				<view class="a">骆驼预览</view>
				<view class="lt">
					<camel-display :items="items"></camel-display>
				</view>
				<view class="diy_button" @click="jump_diy()">
					修改骆驼装扮
				</view>
			</view>

			<view class="box2">
				<view class="box3">
					<view class="detail">
						<view class="aaa">骆驼信息</view>
						<view class="txt">骆驼名字：{{lt_name}}</view>
						<view class="txt">年龄：{{lt_age}}岁</view>
						<view class="txt">体型：{{getBody(lt_body)}}</view>
						<view class="txt">状态：{{lt_zt=="1"?"单身":(lt_zt=="2"?"恋爱中":(lt_zt=="3"?"其它":"未知"))}}</view>
						<view class="txt">最喜欢的食物：{{lt_food}}</view>

						<view class="aaa">主人信息</view>
						<view class="txt">姓名：{{zr_name}}</view>
						<view class="txt">性别：{{zr_sex=="1"?"男":(zr_sex=="2"?"女":(zr_sex=="3"?"其它":"未知"))}}</view>
						<view class="txt">生日：{{zr_sr}}</view>
						<view class="txt">学院：{{zr_xy}}</view>
						<view class="txt">校园卡：{{zr_card}}</view>
						<view class="txt">订单编号：{{order_id}}</view>

					</view>
				</view>
			</view>
			<view class="footer" v-if="isSubmitted">
				<view class="f0" @click="showQRcode">显示二维码</view>
			</view>
			<view class="footer" v-else>
				<view class="f1" @click="qxdd()">删除订单</view>
				<view class="f2" @click="xgdd()">修改订单</view>
				<view class="f1" @click="tjdd()">提交订单</view>
			</view>
			<view style="height: 30px;width: 100vw;"></view>

			<!-- <ul class="bg-bubbles">
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
		</ul> -->

		</view>
	</view>
</template>

<script>
	import camel_display from '@/components/camel-display.vue';
	import itemSprites from 'static/scripts/item-sprites.js';
	export default {
		components: {
			"camel-display": camel_display,
		},
		data() {
			return {
				msg: "",

				lt_name: "",
				lt_age: "",
				lt_body: "",
				lt_zt: "",
				lt_food: "",
				lt_xg: "",

				zr_name: "",
				zr_year: "",
				zr_month: "",
				zr_day: "",
				zr_sr: "",
				zr_sex: "",
				zr_zy: "",
				zr_xy: "",
				zr_card: "",
				order_id: "",

				items: {
					"head": 0,
					"face": 100,
					"neck": 200,
					"seat": 300
				},
				itemSprites: itemSprites,
				userId: '',
				orderId: 0,
				headPossessions: [],
				facePossessions: [],
				neckPossessions: [],
				seatPossessions: [],
				isSubmitted: false, //是否被提交
			};
		},
		onShow() {
			this.userId = getApp().globalData.userId;
			this.orderId = +this.$route.query.order;
			if(this.$route.query.status == 2){
				this.isSubmitted = true;
			}
			this.order_id = this.orderId;
			var that = this
			// getPossessions()
			uni.request({
				url: 'http://127.0.0.1:8000/order/query/' + that.orderId,
				method: "GET",
				success: (res) => {
					//console.log(res.data)
					that.lt_name = res.data.dat.extra.name;
					that.lt_age = res.data.dat.extra.lt_age;
					that.lt_body = res.data.dat.extra.lt_body;
					that.lt_food = res.data.dat.extra.lt_food;
					that.lt_zt = res.data.dat.extra.lt_zt;
					that.zr_name = res.data.dat.extra.zr_name;
					that.zr_card = res.data.dat.extra.zr_card;
					that.zr_sr = res.data.dat.extra.zr_sr;
					that.zr_xy = res.data.dat.extra.zr_xy;
					this.zr_sex = res.data.dat.extra.zr_sex;
					that.items = res.data.dat.items;
				}
			})
		},
		methods: {
			jump_diy() {
				if(this.isSubmitted){
					uni.showToast({
						title:"提交之后不能再修改了噢",
						icon:"error"
					})
					return
				}
				uni.navigateTo({
					url: '/pages/diyzhuangban?order=' + this.orderId + "&mode=modify"
				})
			},
			getBody(status) {
				switch (status) {
					case "1":
						return "胖";
					case "2":
						return "微胖";
					case "3":
						return "瘦";
					case "4":
						return "很瘦";
				}
			},
			showQRcode() {
				uni.navigateTo({
					url: '/pages/qrcode?order=' + this.orderId
				});
			},
			qxdd() {
				console.log("删除订单成功")
				uni.request({
					url: 'http://127.0.0.1:8000/order/delete/',
					data: {
						user_id: this.userId,
						order_id: this.orderId,
					},
					method: 'POST',
					success(res) {
						if (res.data.code == 1) {
							uni.showToast({
								icon: 'success',
								title: '删除订单成功',
							}).then(v => {
								setTimeout(() => {
									uni.hideToast();
									uni.navigateTo({
										url: '/pages/list'
									});
								}, 500)
							})
						} else {
							uni.showToast({
								icon: 'error',
								title: res.data.msg
							}).then(v => {
								setTimeout(() => {
									uni.hideToast()
								}, 500)
							})
							console.log(res.data.msg);
						}
					}

				})
			},
			xgdd() {
				console.log("修改订单");
				// if(this.lt_zt=="1")
				// {
				uni.navigateTo({
					url: '/pages/message?order=' + this.orderId + "&mode=modify"
				})
				// }
				// if(this.lt_zt=="2")
				// {
				// 	uni.navigateTo({
				// 		url: '/pages/modify2?order='+this.orderId
				// 	})
				// }
			},
			tjdd() {
				uni.navigateTo({
					url: '/pages/qrcode?order_id=' + this.orderId
				})
			},
			fanhui() {
				uni.navigateTo({
					url: '/pages/list'
				})
			},
			getPossessions() {
				var that = this;
				uni.request({
					url: getApp().globalData.serverURL + '/order/query/' + this.orderId +
						'?query=*.{possessions|owner.possessions}',
					method: 'GET',
					success(res) {
						that.items = res.data.dat.items;
						var headSet = new Set();
						var faceSet = new Set();
						var neckSet = new Set();
						var seatSet = new Set();
						var filter = e => {
							switch (true) {
								case e < 100:
									headSet.add(e);
									break;
								case e < 200:
									faceSet.add(e);
									break;
								case e < 300:
									neckSet.add(e);
									break;
								default:
									seatSet.add(e);
							}
						};
						//console.log(that.items);
						res.data.dat.owner.possessions.forEach(filter);
						if (res.data.dat.complement != null) {
							res.data.dat.complement.owner.possessions.forEach(filter);
						}
						that.headPossessions = Array.from(headSet);
						that.facePossessions = Array.from(faceSet);
						that.neckPossessions = Array.from(neckSet);
						that.seatPossessions = Array.from(seatSet);
					}
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

	.all {
		display: flex;
		width: 100vw;
		flex-direction: column;
		/* justify-content: center; */
		align-items: center;
	}

	.top {
		background: linear-gradient(to right, #FF6E53 0, #FF6E52, #FF8453, #FF9758, #FFA859 100%);
		width: 100vw;
		height: 160px;
		/* z-index: -7; */
		display: flex;
		align-items: center;
		font-size: 20px;
		color: aliceblue;
		padding-top: 2vw;
		flex-direction: column;
		/* margin-top: 6vh; */
	}

	.box1 {
		display: flex;
		/* justify-content: center; */
		align-items: center;
		/* background-color: aquamarine; */
		width: 100%;
		margin-top: 10px;
		flex-direction: column;
		/* z-index: -5; */

		width: 84vw;
		height: auto;

		margin-top: -90px;
		border-radius: 40px;
		border: none;
		box-shadow: 0 0 50px 3px rgba(0, 0, 0, 0.2);
		background-color: #F5F5F5;
		padding: 2vw;

	}

	.a {
		margin-top: 10px;
		font-size: 40rpx;
	}

	.lt {
		width: 80vw;
		height: 80vw;
		position: relative;
		margin-bottom: 20px;
		/* z-index: -1; */
	}

	.diy_button {
		width: auto;
		height: 10vw;
		padding-left: 15px;
		padding-right: 15px;
		margin-bottom: 15px;
		line-height: 10vw;
		font-size: 40rpx;
		font-weight: 100;
		background: #FF8453;
		color: white;
		/* border: #FF8453 1px solid; */
		border-radius: 10px;
		/* z-index: 99; */

	}
	.box2 {
		display: flex;
		/* z-index: -9; */
		justify-content: center;
	}

	.box3 {
		display: flex;
		background: yellow;
		margin-top: 15px;
		margin-bottom: 25px;
		padding-bottom: 15px;
		/* background: rgb(246, 224, 197); */
		background: linear-gradient(to right, #FF6E53 0, #FF6E52, #FF8453, #FF9758, #FFA859 100%);
		border-radius: 23px 23px 23px 23px;
		width: 88vw;
	}

	.detail {
		margin-top: 12px;
		margin-left: 20px;
		font-size: 13px;
	}

	.aaa {
		margin-top: 10px;
		font-size: 39rpx;
		/* color: rgb(67, 67, 67); */
		color: white;
	}

	.txt {
		margin-top: 2px;
		font-size: 26rpx;
		/* color: rgb(67, 67, 67); */
		color: rgb(255, 251, 226);
	}

	.footer {
		position: fixed;
		/* z-index: 9; */
		bottom: 0;
		width: 100vw;
		height: 40px;
		background: white;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		box-shadow: 0 0px 29px 1px rgba(0, 0, 0, 0.2);
		font-size: 12px;
	}

	.f0 {
		width: 33vw;
		display: flex;
		margin-left: 33vw;
		justify-content: center;
		align-items: center;
	}

	.f1 {
		width: 33vw;
		display: flex;
		/* display: block; */
		justify-content: center;
		align-items: center;
	}

	.f2 {
		width: 33vw;
		display: flex;
		/* display: block; */
		justify-content: center;
		align-items: center;
		border-left: solid 1px rgba(0, 0, 0, 0.1);
		border-right: solid 1px rgba(0, 0, 0, 0.1);
		/* border: 1px solid rgba(0, 0, 0, 0.2); */
	}

	.f0 .f1 .f2 :link {
		background: white;
	}

	.f0 .f1:visited {
		background: #FF6E53;
		color: white;
	}

	.f0 .f1:hover {
		background: #FF6E53;
		color: white;
	}

	.

	/* f2:link{
	    background: white;
	} */
	.f2:visited {
		background: #FF6E53;
		color: white;
	}

	.f2:hover {
		background: #FF6E53;
		color: white;
	}


















	.dd {
		height: 100px;
		width: auto;
		background: white;
		margin-left: 10px;
		margin-right: 10px;
		margin-top: 15px;
		border-radius: 10px;
		box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset, rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
	}

	.status {
		color: rgb(42, 111, 42);
	}



	/* 
	
	
	.bg-bubbles {
	  position: fixed;
	  top: 0;
	  left: 0;
	  width: 100%;
	  height: 100%;
	  z-index: -7;
	}
	.bg-bubbles li {
	  position: absolute;
	  list-style: none;
	  display: block;
	  width: 40px;
	  height: 40px;
	  background-color: rgba(255, 255, 255, 0.35);
	  bottom: -160px;
	  -webkit-animation: square 25s infinite;
	  animation: square 25s infinite;
	  transition-timing-function: linear;
	}
	.bg-bubbles li:nth-child(1) {
	  left: 10%;
	}
	.bg-bubbles li:nth-child(2) {
	  left: 20%;
	  width: 80px;
	  height: 80px;
	  -webkit-animation-delay: 2s;
	          animation-delay: 2s;
	  -webkit-animation-duration: 17s;
	          animation-duration: 17s;
	}
	.bg-bubbles li:nth-child(3) {
	  left: 25%;
	  -webkit-animation-delay: 4s;
	          animation-delay: 4s;
	}
	.bg-bubbles li:nth-child(4) {
	  left: 40%;
	  width: 60px;
	  height: 60px;
	  -webkit-animation-duration: 22s;
	          animation-duration: 22s;
	  background-color: rgba(255, 255, 255, 0.45);
	}
	.bg-bubbles li:nth-child(5) {
	  left: 70%;
	}
	.bg-bubbles li:nth-child(6) {
	  left: 80%;
	  width: 120px;
	  height: 120px;
	  -webkit-animation-delay: 3s;
	          animation-delay: 3s;
	  background-color: rgba(255, 255, 255, 0.4);
	}
	.bg-bubbles li:nth-child(7) {
	  left: 32%;
	  width: 160px;
	  height: 160px;
	  -webkit-animation-delay: 7s;
	          animation-delay: 7s;
	}
	.bg-bubbles li:nth-child(8) {
	  left: 55%;
	  width: 20px;
	  height: 20px;
	  -webkit-animation-delay: 15s;
	          animation-delay: 15s;
	  -webkit-animation-duration: 40s;
	          animation-duration: 40s;
	}
	.bg-bubbles li:nth-child(9) {
	  left: 25%;
	  width: 10px;
	  height: 10px;
	  -webkit-animation-delay: 2s;
	          animation-delay: 2s;
	  -webkit-animation-duration: 40s;
	          animation-duration: 40s;
	  background-color: rgba(255, 255, 255, 0.5);
	}
	.bg-bubbles li:nth-child(10) {
	  left: 90%;
	  width: 160px;
	  height: 160px;
	  -webkit-animation-delay: 11s;
	          animation-delay: 11s;
	}
	@-webkit-keyframes square {
	  0% {
	    transform: translateY(0);
	  }
	  100% {
	    transform: translateY(-700px) rotate(600deg);
	  }
	}
	@keyframes square {
	  0% {
	    transform: translateY(0);
	  }
	  100% {
	    transform: translateY(-700px) rotate(600deg);
	  }
	} */
</style>