<template>
	<view class="container">
		<image
		class="camel" 
		src="/static/images/camel/camel.png"
		mode="widthFix">
			<image
			class="head"
			:src="itemSprites[items.head].foreground.texture"
			:style="'left:'+itemSprites[items.head].foreground.offsetX+'%;top:'+itemSprites[items.head].foreground.offsetY+'%;width:'+itemSprites[items.head].foreground.width+'%;'"
			mode="widthFix"
			></image>
			<image
			class="face"
			:src="itemSprites[items.face].foreground.texture"
			:style="'left:'+itemSprites[items.face].foreground.offsetX+'%;top:'+itemSprites[items.face].foreground.offsetY+'%;width:'+itemSprites[items.face].foreground.width+'%;'"
			mode="widthFix"
			></image>
			<image
			class="neck"
			:src="itemSprites[items.neck].foreground.texture"
			:style="'left:'+itemSprites[items.neck].foreground.offsetX+'%;top:'+itemSprites[items.neck].foreground.offsetY+'%;width:'+itemSprites[items.neck].foreground.width+'%;'"
			mode="widthFix"
			></image>
			<image
			class="seat"
			:src="itemSprites[items.seat].foreground.texture"
			:style="'left:'+itemSprites[items.seat].foreground.offsetX+'%;top:'+itemSprites[items.seat].foreground.offsetY+'%;width:'+itemSprites[items.seat].foreground.width+'%;'"
			mode="widthFix"
			></image>
		</image>
		
	</view>
</template>

<script>
import itemSprites from 'static/scripts/item-sprites.js';
export default{
	name:'camel-display',
	data() {
		return {
			itemSprites : itemSprites,
		}
	},
	props:{
		items:{"head":0, "face":100, "neck":200, "seat":300},
	}
}

</script>

<style>
	.container{
		position: relative;
		width: 100%;
		height: fit-content;
		margin: 0;
		padding: 0;
		border: 0;
	}
	.camel{
		margin: 0;
		padding: 0;
		border: 0;
		width: 100%;
		top: 0;
		left: 0;
	}
	.head{
		position: absolute;
		z-index: 4;
		margin: 0;
		padding: 0;
		border: 0;
	}
	.face{
		position: absolute;
		z-index: 2;
		margin: 0;
		padding: 0;
		border: 0;
	}
	.neck{
		position: absolute;
		z-index: 3;
		margin: 0;
		padding: 0;
		border: 0;
	}
	.seat{
		position: absolute;
		z-index: 1;
		margin: 0;
		padding: 0;
		border: 0;
	}
</style>