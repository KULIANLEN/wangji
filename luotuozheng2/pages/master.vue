<template>
	<form class="form1" action="">
		<view class="formtitle">生日</view>
		<picker mode="date" :value="date" :start="startDate" :end="endDate" @change="bindDateChange">
			<view class="text">{{date}}</view>
		</picker>
	</form>
</template>

<script>
	export default {
		data() {
		        const currentDate = this.getDate({
		            format: true
		        })
		        return {
					sex:'',
		            index: 0,
		            date: currentDate,
		        }
		    },
		    computed: {
		        startDate() {
		            return this.getDate('start');
		        },
		        endDate() {
		            return this.getDate('end');
		        }
		    },
		    methods: {
		        bindDateChange: function(e) {
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
				
		    }
	};
</script>

	<style>
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
			.bg-bubbles {
			  position: fixed;
			  top: 0;
			  left: 0;
			  width: 100%;
			  height: 100%;
			  z-index: 1;
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
			}

	</style>
