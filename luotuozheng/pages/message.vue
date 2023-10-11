<template>
	<view class="bigbox">
		<view class="zuoshang">
			<image src='/static/hhh/jiantou.png' class="icon" @click="fanhui()"></image>
		</view>
		<view class="top">
			<view>骆驼订单</view>
		</view>
		<view class="middlebox2">
			<form id="form1" class='form1' action="" >
				<view class="bigtitle">
					骆驼信息
				</view>
				<view class="formtitle">
					骆驼名字
				</view>

				<input type="text" class="text" name="name" placeholder="请输入名字" id="name" v-model="lt_name" />
				<view class="formtitle">
					年龄
				</view>
				<input type="text" class="text" name="age" placeholder="请输入年龄" id="age" v-model="lt_age" />
				<view class="form">
					<view class="formtitle">
						骆驼体型
					</view>
					<radio-group>
						<label class="radio" @click="handleRadioClick_1(1)">
							<radio id="pang" value="1" name="lt_body" :checked="lt_body === '1' " /><text
								for="pang">胖</text>
						</label>
						<label class="radio1" @click="handleRadioClick_1(2)">
							<radio id="weipang" value="2" name="lt_body" :checked="lt_body === '2' " /><text
								for="weipang">微胖</text>
						</label>
						<label class="radio1" @click="handleRadioClick_1(3)">
							<radio id="shou" value="3" name="lt_body" :checked="lt_body === '3' " /><text
								for="shou">瘦</text>
						</label>
						<label class="radio1" @click="handleRadioClick_1(4)">
							<radio id="henshou" value="4" name="lt_body" :checked="lt_body === '4' " /><text
								for="henshou">很瘦</text>
						</label>
					</radio-group>
				</view>
				<view>
					<view class="formtitle">
						骆驼状态
					</view>
					<radio-group v-model="lt_zt">
						<label class="radio">
							<radio id="pang" value="lt_body1" name="lt_body" checked="1" /><text for="pang">单身</text>
						</label>
					</radio-group>
				</view>
				<view class="formtitle">
					最喜欢的食物
				</view>
				<input type="text" class="text" name="food" placeholder="请输入喜欢的食物" id="food" v-model="lt_food" />
				
			</form>
		</view>
		<view class="box3">
			<form class="form1" action="" >
				<view class="bigtitle">
					主人信息
				</view>
				<view class="formtitle">
					姓名
				</view>
				<input type="text" class="text" name="name" placeholder="请输入姓名" v-model="zr_name" />

				<form class="form1" action="">
					<view class="formtitle">生日</view>
					<picker mode="date" :value="date" :start="startDate" :end="endDate" @change="bindDateChange">
						<view class="text">{{date}}</view>
					</picker>
				</form>

				<view class="formtitle">
					学院
				</view>
				<input type="text" class="text" name="name" v-model="zr_xy" placeholder="请输入学院" />


				<view class="formtitle">
					校园卡号
				</view>
				<input type="text" class="text" name="name" v-model="zr_card" placeholder="请输入校园卡号" />

			</form>





		</view>
		<view class="middlebox3">
			<view class="smallbox2">
				<button class="bottombutton" @click="submitForms">提交信息</button>
			</view>
		</view>

	</view>

</template>


<script>
	export default {
		data() {
			const currentDate = this.getDate({
				format: true
			})
			return {
				sex: '',
				index: 0,
				date: currentDate,
				computed: {
					startDate() {
						return this.getDate('start');
					},
					endDate() {
						return this.getDate('end');
					}
				},
				// body: '',
				// zhuangtai: '',
				activeForm: "form1",
				items: {},
				lt_name: "",
				lt_age: "",
				lt_body: "",
				lt_zt: "1",
				lt_food: "",
				lt_xg: "",

				zr_name: "",
				zr_year: "",
				zr_month: "",
				zr_day: "",
				zr_sex: "",
				zr_zy: "",
				zr_xy: "",
				zr_card: "",
			};
		},
		computed: {
			startDate() {
				return this.getDate('start');
			},
			endDate() {
				return this.getDate('end');
			}
		},
		onShow(){
			this.order_id = this.$route.query.order;
			var arr_items = this.$route.query.items.split("|").map(Number);
			this.items = {
				"head": arr_items[0],
				"face": arr_items[1],
				"neck": arr_items[2],
				"seat": arr_items[3],
			};
			uni.request({
				url: "http://127.0.0.1:8000/order/query/"+this.order_id+"/?query=extra",
				method: "GET",
				success: (res) => {
					var e = res.data.dat.extra;
					this.lt_name = e.name;
					this.lt_age = e.lt_age;
					this.lt_body = e.lt_body;
					this.lt_food = e.lt_food;
					this.zr_name = e.zr_name;
					this.date = e.zr_sr;
					this.zr_xy = e.zr_xy;
					this.zr_card = e.zr_card;
				}
			});
		},
		methods: {
			submitForms() {
				
				if (this.check1() === false) {
					console.log("数据有误");
					uni.showLoading({
					    title: '信息填写不完整'
					});
					setTimeout(() => {
						uni.hideLoading();
					}, 500);
					return null;
				}
				uni.request({
					url: 'http://127.0.0.1:8000/order/modify/',
					data: {
						user_id: getApp().globalData.userId,
						order_id: this.order_id,
						extra:{"name": this.lt_name,
								"lt_age":this.lt_age,
								"lt_body":this.lt_body,
								"lt_zt":"1",
								"lt_food":this.lt_food,
								"zr_name":this.zr_name,
								"zr_sr":this.date,
								"zr_xy":this.zr_xy,
								"zr_card":this.zr_card,
							},
						items:{"head": this.items.head, "face": this.items.face, "neck": this.items.neck, "seat": this.items.seat}
					},
					method: "POST",
					success: (res) => {
						if(res.data.code == 1){
							uni.showToast({
								icon: "success",
								title: "修改成功",
							})
							setTimeout(()=>{uni.navigateTo({
								url:'/pages/list'
							})}, 750);
						} else {
							uni.showToast({
								icon: "error",
								title: "修改失败",
							})
							setTimeout(()=>{uni.hideToast()}, 750);
						}
					}
				})
//////////////////////////////////////////////////////////////////原来的
				// uni.request({
				// 	url: 'http://127.0.0.1:8000/order/modify/',
				// 	data: {
				// 		user_id: "114",
				// 		order_id: that.order_id,
				// 		extra:{"name": this.lt_name,
				// 				"lt_age":this.lt_age,
				// 				"lt_body":this.lt_body,
				// 				"lt_zt":"1",
				// 				"lt_food":this.lt_food,
				// 				"zr_name":this.zr_name,
				// 				"zr_sr":this.date,
				// 				"zr_xy":this.zr_xy,
				// 				"zr_zy":this.zr_zy,
				// 				"zr_card":this.zr_card,
				// 			},
				// 		items:{"head":0, "face":100, "neck":200, "seat":300}
				// 	},
					
				// 	method: "POST",
				// 	success: (res) => {
				// 		console.log(res.data)
				// 		uni.navigateTo({
				// 			url:'/pages/list'
				// 		})
				// 	}
				// })
////////////////////////////////////////////////////////////////////////////////////
				// var formData = {
				// 	name: name,
				// 	age: age,
				// 	food: food,
				// 	xingge: xingge
				// };
				// var jsonData = JSON.stringify(formData);
				// console.log(jsonData)
			},
			fanhui(){
				uni.showModal({
					title: "放弃修改并返回？",
					success: (res)=>{
						if(res.confirm){
							uni.navigateTo({
								url: '/pages/detail?order=' + this.order_id
							})
						}
					}
				})
			},
			handleRadioClick_1(value) {
				this.lt_body = value.toString();
				console.log(this.lt_body)
			},
			handleRadioClick_2(value) {
				this.lt_zt = value.toString();
				console.log(this.lt_zt)
			},
			handleRadioClick_3(value) {
				this.zr_sex = value.toString();
				console.log(this.zr_sex)
			},
			showForm(formName) {
				this.activeForm = formName;
			},
			check1() {
				if (this.lt_name === '' || this.lt_age === '' || this.lt_food === ''  || this.zr_name === ''  || this.zr_xy ===
					'' || this.zr_card === '') {
					return false; // 阻止表单提交
				}

				// 进行其他表单验证逻辑...

				return true; // 允许表单提交
			},
			bindDateChange: function(e) {
				this.date = e.detail.value
			},
			getDabindDateChange: function(e) {
				this.date = e.detail.value
			},
			getDate(type) {
				const date = new Date();
				let year = date.getFullYear();
				let month = date.getMonth() + 1;
				let day = date.getDate();

				if (type === 'start') {
					year = year - 60;
				} else if (type === 'end') {
					year = year + 2;
				}
				month = month > 9 ? month : '0' + month;
				day = day > 9 ? day : '0' + day;
				return `${year}-${month}-${day}`;
			},
			te(type) {
				const date = new Date();
				let year = date.getFullYear();
				let month = date.getMonth() + 1;
				let day = date.getDate();

				if (type === 'start') {
					year = year - 60;
				} else if (type === 'end') {
					year = year + 2;
				}
				month = month > 9 ? month : '0' + month;
				day = day > 9 ? day : '0' + day;
				return `${year}-${month}-${day}`;
			},
		},
	}
</script>
<style>
	.zuoshang {
		position: fixed;
		top: 36rpx;
		left: 15rpx;
	}
	.icon {
		height: 4vh;
		width: 4vh;
		display: flex;
		justify-content: flex-start;
	}
	.formtitle {
		/* text-indent: 1em; */
		color: #FFA859;
		margin-top: 2vh;
		font-weight: 550;
		font-size: 30rpx;
		margin-bottom: 1vh;
	
	}
	.bigtitle {
		/* text-indent: 1em; */
		display: flex;
		justify-content: center;
		color: rgb(90,90,90);
		margin-top: 2vh;
		font-weight: bold;
		font-size: 35rpx;
		margin-bottom: 1vh;
	
	}
	.text {
		width: 66vw;
		height: 3vh;
		
		font-size: 28rpx;

		border-width: 1px;
		/* color: rgb(150, 150, 150); */

		border-bottom: solid 1px rgb(200, 200, 200);;
		margin-top: 1vh;
		/* margin: 1vw; */
		
	}
	.text::placeholder{
		color: red;
	}
/* 	.placeholder-stlye{
		color: red;
	} */
	.bigbox {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.top{
		background: linear-gradient(to   right,#FF6E53 0 , #FF6E52 , #FF8453  , #FF9758  ,#FFA859 100% );
		width: 100vw;
		height: 160px;
		/* z-index: -7; */
		display: flex;
		align-items: center;
		font-size: 20px;
		color: white;
		padding-top: 2vw;
		flex-direction: column;
		/* margin-top: 6vh; */
	}

	.background {
		background: linear-gradient(to right, #FF6E53 0, #FF6E52, #FF8453, #FF9758, #FFA859 100%);
		width: 100vw;
		height: 30vh;
		/* z-index: -5; */
		padding-top: 2vh;
		display: flex;
		flex-direction: column;
		align-items: center;
		/* margin-top: 6vh; */
	}


	.smallbox {
		width: 25vw;
		height: 6vh;
		margin-bottom: 10vw;
	}
	.middlebox2 {
		width: 85vw;
		height: auto;
		margin-top: -13vh;
		padding-top: 3vh;
		padding-bottom: 5vh;
		/* padding-left: 5vw; */
		/* padding-right: 1vh; */
		border-radius: 30px;
		border: none;
		box-shadow: 0 0 50px 3px rgba(0, 0, 0, 0.2);
		background-color: rgb(255, 255, 255);
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.box3 {
		width: 85vw;
		height: auto;
		
		margin-top: 5vh;
		margin-bottom: 4vh;
		
		padding-top: 3vh;
		padding-bottom: 5vh;
		/* padding-left: 1vh;
		padding-right: 1vh; */
		border-radius: 30px;
		border: none;
		box-shadow: 0 0 50px 3px rgba(0, 0, 0, 0.2);
		background-color: rgb(255, 255, 255);
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.form1 {
		width: 100%;
		display: flex;
		justify-content: center;
	}
	.radio1 {
		margin-left: 5vw;
		font-size: 28rpx;
	}
	.radio {
		/* margin-left: 3vw; */
		font-size: 28rpx;
	}
	.bottombutton {
		width: 86vw;
		text-align: center;
		border-radius: 15px;
		background: linear-gradient(to bottom right, #FF6E53 0, #FF6E52, #FF8453, #FF9758, #FFA859 100%);
		color: #393232;
		border: none;
		box-shadow: 0 0px 29px 1px rgba(0, 0, 0, 0.2);
		color: white;
	}
	.middlebox3{
		margin-bottom: 2vh;
	}
</style>