<template>
	<view class="bigbox">
		<view class="zuoshang">
			<image src='/static/hhh/jiantou.png' class="icon" @click="fanhui()"></image>
		</view>
		<view class="top">

		</view>

		<view class="background">
			<view class="title">
				情侣骆驼订单
			</view>
			<view class="middlebox1">
				<view class="smallbox">
					<button class="button1" @click="showForm('form1') ">

						骆驼信息
					</button>

				</view>
				<view class="smallbox">
					<button class="button1" @click="showForm('form2')">
						主人信息
					</button>
					
				</view>
				<view class="smallbox">
					<button class="button1" @click="showForm('form3')">邀请码</button>
				</view>


			</view>



		</view>
		<view class="middlebox2">
			<form id="form1" class='form1' action="" v-show="activeForm === 'form1'" onsubmit="return check1()"
				ref="form1">
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
							<radio id="weipang" value="lt_body2" name="lt_body" checked="1" /><text
								for="weipang">恋爱中</text>
						</label>
					</radio-group>
				</view>
				<view class="formtitle">
					最喜欢的食物
				</view>
				<input type="text" class="text" name="food" placeholder="请输入喜欢的食物" id="food" v-model="lt_food" />
			
			</form>


			<form class="form1" action="" v-show="activeForm === 'form2'">
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
			
			<form v-show="activeForm === 'form3'" class="form1">
							<view class="yaoqing">
								<text class="yaoqingtitle">请输入邀请码</text>
								<view class="yaoqingbox">
								   <input type="text"  placeholder="请输入邀请码" >	
								</view>
							</view>
							
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

				lt_name: "",
				lt_age: "",
				lt_body: "",
				lt_zt: "2",
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
			//this.order_id = this.$route.query.order;
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
				// console.log(this.name);
				// console.log(this.lt_age);
				// console.log(this.zr_xy);
				// console.log(this.zr_sex);
				// console.log(this.zr_year)
				var that = this;
				uni.request({
					url: 'http://127.0.0.1:8000/order/create/',
					data: {
						user_id: "114"
					},
					method: "POST",
					success: (res) => {
						console.log(res.data)
						this.order_id=res.data.dat
						uni.request({
							url: 'http://127.0.0.1:8000/order/modify/',
							data: {
								user_id: "114",
								order_id: that.order_id,
								extra:{"name": this.lt_name,
										"lt_age":this.lt_age,
										"lt_body":this.lt_body,
										"lt_zt":"2",
										"lt_food":this.lt_food,
										"zr_name":this.zr_name,
										"zr_sr":this.date,
										"zr_xy":this.zr_xy,
										"zr_card":this.zr_card,
									},
								items:{"head":0, "face":100, "neck":200, "seat":300}
							},
							method: "POST",
							success: (res) => {
								console.log(res.data)
								uni.navigateTo({
									url:'/pages/list'
								})
							}
						})
					}
				})

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
				uni.navigateTo({
					url:'/pages/choose'
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
		top: 16rpx;
		left: 15rpx;
	}
	.icon {
		height: 4vh;
		width: 4vh;
		display: flex;
		justify-content: flex-start;
	}
		.text{
			width: 66vw;
			height: 3vh;
			
			border-width: 1px;
			
			
			border-bottom:solid 1px #BEBDBF;
			margin-top: 1vw;
			/* margin: 1vw; */	
		}
		text::-moz-placeholder {
			  color:  red;
			}
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
	.bigbox {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.top {
		width: 100vw;
		height: 6vh;
		z-index: -1;
		background: linear-gradient(to right, #FF6E53 0, #FF6E52, #FF8453, #FF9758, #FFA859 100%);
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

	.title {
		font-size: 2vh;
		font-weight: bold;
		align-self: flex-start;
		text-indent: 2em;
		color: #fff1cf;



	}

	.middlebox1 {
		display: flex;
		justify-content: space-around;
		width: 94vw;
		height: 5vh;
		margin-top: 5vh;

	}

	.smallbox {


		width: 25vw;
		height: 6vh;
		margin-bottom: 10vw;
	}

	.button1 {
		height: 5vh;
		text-align: center;

		background-color: #f8f4e6;
		color: #494a41;
		border-radius: 5px;
		border: none;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
		font-size: 1rem;
		z-index: 99999999;
	}

	button1:active {
		background-color: red;
	}





	.middlebox2 {
		width: 84vw;
		height: auto;

		margin-top: -13vh;
		border-radius: 40px;
		border: none;
		box-shadow: 0 0 50px 3px rgba(0, 0, 0, 0.2);
		background-color: #F5F5F5;
		display: flex;
		flex-direction: column;
		padding: 2vw;
		align-items: center;


	}

	.formtitle {
		/* text-indent: 1em; */
		color: #808080;
		margin-top: 4vw;
		font-size: 1rem;
		margin-bottom: 1vw;

	}

	.text {
		width: 66vw;
		height: 3vh;

		border-width: 1px;


		border-bottom: solid 1px #BEBDBF;
		margin-top: 1vw;
		/* margin: 1vw; */
	}

	.form {
		margin-top: 2vw;
	}

	.radio1 {
		margin-left: 5vw;

	}

	.middlebox3 {
		margin-top: 7vw;
		width: 100vw;
		height: 10vh;
	}

	.smallbox2 {
		width: 100vw;
		height: 15vh;
	}

	.bottombutton {
		width: 90vw;
		text-align: center;
		border-radius: 15px;
		background: linear-gradient(to bottom right, #FF6E53 0, #FF6E52, #FF8453, #FF9758, #FFA859 100%);
		color: #393232;
		border: none;
		box-shadow: 0 0px 29px 1px rgba(0, 0, 0, 0.2);
		color: #fff1cf;
	}
	
		.yaoqing{
			text-align: center;
		}
		.yaoqingtitle{
			font-size: 10vw;
			
		}
		.yaoqingbox{
			height: 5vh;
			border: none;
			border-radius: 4px;
			width: 50vw;
			outline: none;
			font-size: 12px;
			background-color: #f5f5f5;
			color: #444444;
			box-shadow: inset 0 2px 4px rgba(0, 0, 0, .2);
			margin-top: 10vw;
			margin-left: 5vw;
			margin-bottom: 10vw;
		}
</style>