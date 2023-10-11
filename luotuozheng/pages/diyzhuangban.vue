<template>
	<view>
		<view class="zuoshang">
			<image src='/static/hhh/jiantou.png' class="icon" @click="fanhui()"></image>
		</view>
		<view class="bigbox">
			<view class="top">
				<view class="backcolor">
					<!-- <view class="middlebox2">
					<view class="smallbox">
						<button class="topbutton" @click="jump1()">装扮图鉴</button>
					</view>
					<view class="smallbox">
						<button class="topbutton" @click="jump2()">去抽卡</button>
					</view>
					<view class="smallbox">
						<button class="topbutton" @click="jump3()">填写信息</button>
					</view>
				</view> -->
					<view class="middlebox3">
						<camel-display :items="items"></camel-display>
					</view>
					<view class="middlebox4" v-show="page===1">
						<view class="items_container">
							<view class="image" v-for="(el, idx) in headPossessions" :key="idx"
								@click="selectItem('head', el)">
								<image mode="widthFix" :src="itemSprites[el].foreground.texture"
									:style="'left:'+itemSprites[el].item_display.offsetX+'%;top:'+itemSprites[el].item_display.offsetY+'%;width:'+itemSprites[el].item_display.width+'%;'">
								</image>
							</view>
						</view>
					</view>
					<view class="middlebox4" v-show="page===2">
						<view class="items_container">
							<view class="image" v-for="(el, idx) in facePossessions" :key="idx"
								@click="selectItem('face', el)">
								<image mode="widthFix" :src="itemSprites[el].foreground.texture"
									:style="'left:'+itemSprites[el].item_display.offsetX+'%;top:'+itemSprites[el].item_display.offsetY+'%;width:'+itemSprites[el].item_display.width+'%;'">
								</image>
							</view>
						</view>
					</view>
					<view class="middlebox4" v-show="page===3">
						<view class="items_container">
							<view class="image" v-for="(el, idx) in neckPossessions" :key="idx"
								@click="selectItem('neck', el)">
								<image mode="widthFix" :src="itemSprites[el].foreground.texture"
									:style="'left:'+itemSprites[el].item_display.offsetX+'%;top:'+itemSprites[el].item_display.offsetY+'%;width:'+itemSprites[el].item_display.width+'%;'">
								</image>
							</view>
						</view>
					</view>
					<view class="middlebox4" v-show="page===4">
						<view class="items_container">
							<view class="image" v-for="(el, idx) in seatPossessions" :key="idx"
								@click="selectItem('seat', el)">
								<image mode="widthFix" :src="itemSprites[el].foreground.texture"
									:style="'left:'+itemSprites[el].item_display.offsetX+'%;top:'+itemSprites[el].item_display.offsetY+'%;width:'+itemSprites[el].item_display.width+'%;'">
								</image>
							</view>
						</view>
					</view>
					<view class="middlebox5">

						<view class="smallbox2" @click="change(1)">
							<button class="underbutton">帽子</button>
						</view>
						<view class="smallbox2" @click="change(2)">
							<button class="underbutton">面部</button>
						</view>
						<view class="smallbox2" @click="change(3)">
							<button class="underbutton">颈部</button>
						</view>
						<view class="smallbox2" @click="change(4)">
							<button class="underbutton">坐垫</button>
						</view>

					</view>
				</view>
				<view class="confirm-button" @click="confirm()">下一步</view>
			</view>
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
				mode: 'create', //create or modify
				page: 1,
				items: {
					"head": 0,
					"face": 100,
					"neck": 200,
					"seat": 300
				},
				itemSprites: itemSprites,
				userId: '',
				orderId: 0,
				headPossessions: [1, 2, 3, 4, 5, 6, 7, 8, 0],
				facePossessions: [101, 102, 103, 104, 100],
				neckPossessions: [201, 202, 203, 200],
				seatPossessions: [301, 302, 303, 304, 300],
			}
		},
		onShow() {
			this.userId = getApp().globalData.userId;
			this.orderId = +this.$route.query.order;
			this.mode = this.$route.query.mode
			var that = this
			if (this.mode == 'modify') {
				uni.request({
					url:'http://127.0.0.1:8000/order/query/'+that.orderId,
					method:"GET",
					success : (res)=>{
						// console.log(res.data)
						console.log(res.data.dat.items)
						// that.items.head=res.data.dat.items.name;
						// that.items.face=res.data.dat.items.face;
						// that.items.neck=res.data.dat.items.neck;
						// that.items.seat=res.data.dat.items.seat;
						that.items=res.data.dat.items;
						console.log(that.items)
						// this.zr_name=res.data.dat.extra.zr_name;
						// this.zr_card=res.data.dat.extra.zr_card;
						// this.zr_sr=res.data.dat.extra.zr_sr;
						// this.zr_xy=res.data.dat.extra.zr_xy;
					}
				})
			}

		},
		methods: {
			jump1() {
				uni.navigateTo({
					url: '/pages/list'
				})
			},
			jump2() {
				uni.navigateTo({
					url: '/pages/chouka'
				})
			},
			jump3() {
				uni.navigateTo({
					url: '/pages/master'
				})
			},

			change(pageid) {
				this.page = pageid;
			},
			selectItem(slot, item) {
				this.items[slot] = item;
				this.$forceUpdate();
			},
			fanhui() {
				var that = this
				uni.showModal({
					content:"放弃修改并返回？",
					success(res) {
						if(res.confirm){
							uni.navigateTo({
								url: '/pages/detail?order=' + that.orderId
							})
						}
						
					}
				})
				// if (window.confirm("放弃修改并返回？"))
				// 	uni.navigateTo({
				// 		url: '/pages/detail?order=' + this.orderId
				// 	})
			},
			confirm() {
				if (this.mode == 'create') {
					uni.navigateTo({
						url: "/pages/message?order=" + this.orderId + "&items=" + String(this.items.head) + "|" +
							String(this.items.face) + "|" +
							String(this.items.neck) + "|" + String(this.items.seat)+"&mode=create"
					})
				}else if (this.mode == 'modify'){
					var that = this
					uni.request({
						url: 'http://127.0.0.1:8000/order/modify/',
						data: {
							user_id: getApp().globalData.userId,
							order_id: that.orderId,
							items:{
								"head": that.items.head,
								"face": that.items.face,
								"neck": that.items.neck,
								"seat": that.items.seat,
							}
						},
						method: "POST",
						success: (res) => {
							if (res.data.code == 1) {
								uni.showToast({
									icon: "success",
									title: "修改成功",
								})
								setTimeout(() => {
									uni.navigateTo({
										url: "/pages/detail?order=" + that.orderId 
									})
								}, 750);
							} else {
								uni.showToast({
									icon: "error",
									title: "修改失败" + res.data.msg,
								})
								setTimeout(() => {
									uni.hideToast()
								}, 750);
							}
						}
					})
					
				}

			},
			getPossessions() {
				var that = this;
				uni.request({
					url: 'http://127.0.0.1:8000/order/query/' + this.orderId +
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

	}
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

	* {
		margin-right: 1vw;
	}

	.top {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 100vw;
		height: 8vh;
		z-index: -2;
		background: linear-gradient(to right, #FF6E53, #FF6E52, #FF8453 40%, #FF9758, #FFA859);
	}

	.backcolor {

		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		width: 100vw;
		height: 100vh;
		background-image: linear-gradient(to left, #FFE7AC, #FFBF90);
		margin-top: 15vw;

		border-radius: 5% 100% 0 100%;

	}

	.topbutton {
		background: linear-gradient(to bottom right, #FF6E53 0, #FF6E52, #FF8453, #FF9758, #FFA859 100%);
		color: #393232;
		border: none;
		box-shadow: 0 0px 29px 1px rgba(0, 0, 0, 0.2);
		color: #fff1cf;
		background-color: #f8f3d4;
		color: #393232;
		border-radius: 15px;
		border: none;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
		z-index: 999;
		font-size: 35rpx;
	}

	.bigbox {


		background-color: #F5F5F5;
		width: 100vw;
		height: 110vh;

		z-index: -2;


	}

	.middlebox1 {
		margin-left: 2vw;
		width: 94vw;
		height: 4vh;
		border: 1px;
		border-style: solid;
		border-color: #808080;
		display: flex;
		border-radius: 4px;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
	}

	.middlebox2 {
		margin-left: 2vw;
		width: 94vw;
		height: 11vh;
		border: 1px;
		border-style: solid;
		border-color: #808080;
		margin-top: 4vw;
		display: flex;
		justify-content: center;
		align-items: center;
		border-radius: 4px;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
	}

	.smallbox {
		margin: 1vw;
		width: 34vw;
		/* border-radius: 8px; */
	}

	.back {
		border-style: solid;
		border-color: #808080;
		width: 6vw;
	}

	.middlebox3 {
		position: relative;
		margin-left: 2vw;
		margin-top: 5vw;
		padding: 1vw;
		border: 1px;
		border-style: solid;
		border-color: #808080;
		width: 93vw;
		height: 45vh;
		border-radius: 4px;
		background-color: #F5F5F5;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.3);

	}

	.middlebox4 {
		margin-left: 2vw;
		margin-top: 5vw;
		border: 1px;
		border-style: solid;
		border-color: #808080;
		width: 94vw;
		height: 20vw;
		border-radius: 4px;
		overflow-x: scroll;
		overflow-y: hidden;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.1);
	}

	.items_container {
		margin-top: 2.25vw;
		padding: 0;
		width: fit-content;
		height: 100%;
		display: flex;
		justify-content: center;
		flex-direction: row;
	}

	.middlebox5 {
		margin-left: 2vw;
		margin-top: 4vw;
		display: flex;
		justify-content: space-around;
		align-items: center;
		border: 1px;
		border-style: solid;
		border-color: #808080;
		width: 94vw;
		height: 7vh;
		border-radius: 4px;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.1);

	}

	.image {
		height: 15vw;
		width: 15vw;
		border: 1px;
		border-style: solid;
		border-color: #808080;
		margin-left: 3vw;
		margin-right: 3vw;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.1);
	}

	.underbutton {
		/* margin-right: 3vw; */
		margin-top: 2vw;
		height: 5vh;
		width: 20vw;
		background-color: #f8f3d4;
		color: #393232;
		border-radius: 15px;
		border: none;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
		z-index: 999;
		display: flex;
		justify-content: center;
		align-items: center;

	}

	.smallbox2 {
		width: 20vw;
		height: 7vh;
	}

	.confirm-button {
		background: linear-gradient(to bottom right, #FF6E53 0, #FF6E52, #FF8453, #FF9758, #FFA859 100%);
		color: #393232;
		border: none;
		box-shadow: 0 0px 29px 1px rgba(0, 0, 0, 0.2);
		color: #fff1cf;
		/* margin: 7.5%; */
		margin-top: 7.5%;
		width: 85%;
		height: 30vw;
		display: flex;
		justify-content: center;
		align-content: center;
		background-color: #f8f3d4;
		border-radius: 15px;
		border: none;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
	}
</style>