//[0, 1, 2, 3, 4, 5, 6, 7, 8, 100, 101, 102, 103, 104, 200, 201, 202, 203, 300, 301, 302, 303, 304]


const itemSprites = {
	"0": {
		foreground:{
			texture: "",
			offsetX: 0,
			offsetY: 0,
			width : 0,
		},
		item_display:{
			offsetX: 0,
			offsetY: 0,
			width: 0,
		}
	},
	"1": {	
		foreground:{
			texture : "/static/images/head/blue-hair.png",
			offsetX : 4.75,
			offsetY : 7.8,
			width : 40,
		},
		item_display:{
			offsetX: -10,
			offsetY: 10,
			width: 190,
		}
	},	
	"2":{
		foreground:{
			texture : "/static/images/head/flower-ring.png",
			offsetX : 3.75,
			offsetY : 11.75,
			width : 25,
		},
		item_display:{
			offsetX: -50,
			offsetY: 10,
			width: 190,
		}
	},
	"3":{
		foreground:{
			texture : "/static/images/head/003.png",
			offsetX : 5.67,
			offsetY : 6.75,
			width : 25,
		},
		item_display:{
			offsetX: -30,
			offsetY: -20,
			width: 165,
		}
	},
	"4":{
		foreground:{
			texture : "/static/images/head/004.png",
			offsetX : 4.00,
			offsetY : 5.30,
			width : 27,
		},
		item_display:{
			offsetX: -30,
			offsetY: -20,
			width: 180,
		}
	},
	"5":{
		foreground:{
			texture : "/static/images/head/005.png",
			offsetX : 5.75,
			offsetY : 9.00,
			width : 25,
		},
		item_display:{
			offsetX: 0,
			offsetY: 0,
			width: 100,
		}
	},
	"6":{
		foreground:{
			texture : "/static/images/head/006.png",
			offsetX : 6.25,
			offsetY : 3.75,
			width : 25,
		},
		item_display:{
			offsetX: 30,
			offsetY: 0,
			width: 100,
		}
	},
	"7":{
		foreground:{
			texture : "/static/images/head/007.png",
			offsetX : 4.75,
			offsetY : 4.75,
			width : 25,
		},
		item_display:{
			offsetX: 30,
			offsetY: 0,
			width: 100,
		}
	},
	"8":{
		foreground:{
			texture : "/static/images/head/008.png",
			offsetX : 4.25,
			offsetY : 0,
			width : 25,
		},
		item_display:{
			offsetX: 30,
			offsetY: 0,
			width: 100,
		}
	},
	"100":{
		foreground:{
			texture: "/static/images/face/100.png",
			offsetX : 0,
			offsetY : 0,
			width : 100,
		},
		item_display:{
			offsetX: -30,
			offsetY: -50,
			width: 500,
		}
	},
	"101":{
		foreground:{
			texture : "/static/images/face/101.png",
			offsetX : 0,
			offsetY : 0,
			width : 100,
		},
		item_display:{
			offsetX: -30,
			offsetY: -50,
			width: 500,
		}
	},
	"102":{
		foreground:{
			texture : "/static/images/face/102.png",
			offsetX : 0,
			offsetY : 0,
			width : 100,
		},
		item_display:{
			offsetX: -30,
			offsetY: -50,
			width: 500,
		}
	},
	"103":{
		foreground:{
			texture : "/static/images/face/103.png",
			offsetX : 0,
			offsetY : 1,
			width : 100,
		},
		item_display:{
			offsetX: -30,
			offsetY: -50,
			width: 500,
		}
	},
	"104":{
		foreground:{
			texture : "/static/images/face/104.png",
			offsetX : 0,
			offsetY : 0,
			width : 100,
		},
		item_display:{
			offsetX: -30,
			offsetY: -50,
			width: 500,
		}
	},
	"200":{
		foreground:{
			texture: "",
			offsetX: 0,
			offsetY: 0,
			width : 0,
		},
		item_display:{
			offsetX: 0,
			offsetY: 0,
			width: 0,
		}
	},
	"201":{
		foreground:{
			texture : "/static/images/neck/201.png",
			offsetX : 8.75,
			offsetY : 32.75,
			width : 20,
		},
		item_display:{
			offsetX: 0,
			offsetY: 0,
			width: 100,
		}
	},
	"202":{
		foreground:{
			texture : "/static/images/neck/202.png",
			offsetX : 10.75,
			offsetY : 28.75,
			width : 25,
		},
		item_display:{
			offsetX: 0,
			offsetY: 0,
			width: 100,
		}
	},
	"203":{
		foreground:{
			texture : "/static/images/neck/203.png",
			offsetX : 4.75,
			offsetY :22.75,
			width : 40,
		},
		item_display:{
			offsetX: 0,
			offsetY: 0,
			width: 100,
		}
	},
	"300":{
		foreground:{
			texture: "",
			offsetX: 0,
			offsetY: 0,
			width : 0,
		},
		item_display:{
			offsetX: 0,
			offsetY: 0,
			width: 0,
		}
	},
	"301":{
		foreground:{
			texture : "/static/images/seat/301.png",
			offsetX : 43.50,
			offsetY : 22.25,
			width : 25,
		},
		item_display:{
			offsetX: 0,
			offsetY: 0,
			width: 100,
		}
	},
	"302":{
		foreground:{
			texture : "/static/images/seat/302.png",
			offsetX : 50.50,
			offsetY : 5.25,
			width : 25,
		},
		item_display:{
			offsetX: 0,
			offsetY: 0,
			width: 100,
		},
	},
	"303":{
		foreground:{
			texture : "/static/images/seat/303.png",
			offsetX : 42.50,
			offsetY : 26.25,
			width : 25,
		},
		item_display:{
			offsetX: 0,
			offsetY: 0,
			width: 100,
		}
	},
	"304":{
		foreground:{
			texture : "/static/images/seat/304.png",
			offsetX : 43.75,
			offsetY : 18.25,
			width : 25,
		},
		item_display:{
			offsetX: 0,
			offsetY: 0,
			width: 100,
		}
	},
	"300":{
		foreground:{
			texture : "",
			offsetX : 0,
			offsetY : 0,
			width : 0,
		},
		item_display:{
			offsetX: 0,
			offsetY: 0,
			width: 0,
		}
	},
}
export default itemSprites;