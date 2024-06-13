/**  NUI v2.0.0  |  Made by NTELS ICS Team **/

/* Apexcharts options type */

// Legend - position:right 인 경우 마우스 오버시 tooltip 표시 숨김
function hoverLegendTooltip() {
	$('.apx-legend-position-right').hover(function(){
		$(this).parents('.apexcharts-canvas').find('.apexcharts-tooltip').addClass('hidden');
	}, function(){
		$(this).parents('.apexcharts-canvas').find('.apexcharts-tooltip').removeClass('hidden');
	})
}

// statistics page
var optionsLine01 = {
	series: [{
		name: 'Chart Name #01',
		data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10]
	}, {
		name: 'Chart Name #02',
		data: [35, 41, 62, 42, 13, 18, 29, 37, 36, 51, 32, 35]
	}, {
		name: 'Chart Name #03_테스트 텍스트 길이가 긴 경우 테스트',
		data: [87, 57, 74, 99, 75, 38, 62, 47, 82, 56, 45, 47]
	}, {
		name: '차트 Chart Name #04',
		data: [40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]
	}, {
		name: 'Chart Name #05',
		data: [35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35]
	}, {
		name: 'Chart Name #06',
		data: [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
	}, {
		name: 'Chart Name #07',
		data: [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
	}, {
		name: 'Chart Name #08',
		data: [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
	}, {
		name: 'Chart Name #09',
		data: [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
	}, {
		name: 'Chart Name #10',
		data: [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
	}],
	chart: {
		type: 'line',
		height: '100%',
		fontFamily: 'inherit',
		zoom: {
			type: 'x',
			enabled: true,
			autoScaleYaxis: true
		},
		toolbar: {
			// show: false, //Legend - position:Right 인 경우 위치 이슈로 숨김
			offsetX: -20,
			offsetY: 16,
			tools: {
				download: false,
				selection: false,
				zoom: true,
				zoomin: true,
				zoomout: true,
				pan: false,
				reset: ' '
			}
		},
		events: {
			// Legend - position:right 인 경우 마우스 오버시 tooltip 표시 숨김
			updated: function(chartContext, config) { 
				hoverLegendTooltip();
			},
			mounted: function(chartContext, config) {
				hoverLegendTooltip();
			}
		}
	},
	colors: ['#3c91ff', '#37d1a6', '#f1793b', '#8b7dfc', '#e6a712', '#f54b9d', '#2a38ff', '#30cc64', '#ffc02a', '#20ab85'],
	grid: {
		show: false,
		row: {
			colors: ['rgba(138,144,153,0.07', 'transparent'],
			opacity: 1
		},
		padding: {
			top: -15
		}
	},
	dataLabels: {
		enabled: false
	},
	stroke: {
		curve: 'straight',
		width: [2, 2, 2, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
		dashArray: [0, 0, 0, 3, 3, 3, 3, 3, 3, 3]
	},
	legend: {
		position: 'bottom',
		fontSize: '13px',
		labels: {
			colors: '#555555'
		},
		markers: {
			width: 8,
			height: 8,
			radius: 0,
			// offsetX: -17, // position:right 인 경우 offsetX: -17 옵션 추가
		},
		itemMargin: {
			horizontal: 20,
			vertical: 2
		}
	},
	markers: {
		size: 0,
		hover: {
			sizeOffset: 5
		}
	},
	xaxis: {
		// type: 'datetime',
		categories: ['12:00', '12:05', '12:10', '12:15', '12:20', '12:25', '12:30', '12:35', '12:40', '12:45', '12:50', '12:55'],
		labels: {
			offsetY: -1,
			style: {
				colors: '#555555',
				fontSize: '11px'
			},
		},
		axisBorder: {
			color: '#d9d9d9',
		},
		axisTicks: {
			show: false
		}
	},
	yaxis: {
		min: 0,
		max: 110,
		labels: {
			offsetX: -3,
			style: {
				colors: '#555555',
				fontSize: '11px'
			}
		}
	}
};


// dashboard
var optionsDashLine01 = {
	series: [{
		name: 'Inbound',
		data: [45, 40, 38, 24, 33, 81, 26, 20, 6, 8, 15, 10]
	}, {
		name: 'Outbound',
		data: [87, 57, 74, 99, 75, 38, 62, 47, 82, 56, 45, 47]
	}],
	chart: {
		// type: 'line',
		type: 'area',
		height: '100%',
		fontFamily: 'inherit',
		animations: {
			// enabled: false,
			speed: 600,
			easing: 'easeout',
			animateGradually: {
				delay: 30
			}
		},
		zoom: {
			enabled: false
		},
		toolbar: {
			show: false
		},
	},
	annotations: {
		yaxis: [{
			y: 50,
			strokeDashArray: 3,
			borderColor: '#ff0000',
			label: {
				text: 'Threshold: 50',
				borderWidth: 0,
				offsetX: -4,
				style: {
					color: '#ff0000',
					fontSize: '11px',
					background: 'transparent'
				}
			}
		}],
		points: [{
			x: '12:15',
			y: 99,
			marker: {
				size: 3,
				strokeWidth: 2,
				strokeColor: '#35c8e5',
				fillColor: '#ffffff',
			},
			label: {
				borderColor: '#35c8e5',
				borderRadius: 8,
				offsetY: -2,
				style: {
					background: '#35c8e5',
					color: '#fff',
					fontSize: '11px',
					fontFamily: 'inherit',
					cssClass: 'apexcharts-point-annotation-label',
					padding: {
						left: 5,
						right: 5,
						top: 0,
						bottom: 1,
					}
				},
				text: '99',
			}
		}, {
			x: '12:25',
			y: 81,
			marker: {
				size: 3,
				strokeWidth: 2,
				strokeColor: '#5152f8',
				fillColor: '#ffffff',
			},
			label: {
				borderColor: '#5152f8',
				borderRadius: 8,
				offsetY: -2,
				style: {
					background: '#5152f8',
					color: '#fff',
					fontSize: '11px',
					fontFamily: 'inherit',
					cssClass: 'apexcharts-point-annotation-label',
					padding: {
						left: 5,
						right: 5,
						top: 0,
						bottom: 1,
					}
				},
				text: '81',
			}
		}]
	},
	colors: ['#5152f8', '#35c8e5'],
	grid: {
		show: false,
		row: {
			colors: ['rgba(138,144,153,0.07', 'transparent'],
			opacity: 1
		},
		padding: {
			top: -18
		}
	},
	dataLabels: {
		enabled: false
	},
	stroke: {
		curve: 'straight',
		width: 2,
		// dashArray: [0, 0, 0, 3, 3, 3, 3, 3, 3, 3]
	},
	fill: {
		type: 'gradient',
		gradient: {
			shadeIntensity: 1,
			inverseColors: false,
			opacityFrom: 0.55,
			opacityTo: 0,
			stops: [0, 100]
		},
	},
	legend: {
		position: 'bottom',
		fontSize: '12px',
		labels: {
			colors: '#666666'
		},
		markers: {
			width: 14,
			height: 2,
			radius: 0,
		},
		itemMargin: {
			horizontal: 20,
			vertical: 2
		}
	},
	markers: {
		size: 0,
		hover: {
			sizeOffset: 5
		}
	},
	xaxis: {
		categories: ['12:00', '12:05', '12:10', '12:15', '12:20', '12:25', '12:30', '12:35', '12:40', '12:45', '12:50', '12:55'],
		labels: {
			offsetY: -4,
			style: {
				colors: '#aaaaaa',
				fontSize: '10px'
			},
		},
		axisBorder: {
			color: '#e6e6e6',
		},
		axisTicks: {
			show: false
		}
	},
	yaxis: {
		min: 0,
		max: 120,
		labels: {
			offsetX: -3,
			style: {
				colors: '#aaaaaa',
				fontSize: '11px'
			}
		}
	}
};

var optionsDashPie01 = {
	series: [44, 55, 35, 3],
	labels: ['Team A', 'Team B', 'Team C', 'Team D'],
	chart: {
		type: 'donut',
		// type: 'pie',
		height: '100%',
		animations: {
			// enabled: false,
			speed: 600,
		}
	},
	// colors: ['#3c91ff', '#37d1a6', '#f1793b', '#e6a712', '#8b7dfc', '#f54b9d', '#2a38ff', '#30cc64', '#ffc02a', '#20ab85'],
	colors: ['#37d1a6', '#5152f8', '#1da7ff', '#ff694a', '#ffa0a0', '#9051f8', '#ffae4a', '#69cedf', '#c8c8c8'],
	plotOptions: {
		pie: {
			customScale: 0.9,
			expandOnClick: false,
			donut: {
				size: '50%',
				labels: {
					show: true,
					name: {
						show: true,
						offsetY: -10,
					},
					value: {
						show: true,
						fontSize: '22px',
						fontFamily: 'inherit',
						fontWeight: 700,
						color: '#000000',
						offsetY: 3,
					},
					total: {
						show: true,
						showAlways: true,
						label: '합계',
						fontSize: '16px',
						fontFamily: 'inherit',
						fontWeight: 600,
						color: '#000000',
					},
				}
			}
		}
	},
	stroke: {
		width: 0,
	},
	legend: {
		position: 'bottom',
		fontSize: '13px',
		labels: {
			colors: '#555555'
		},
		markers: {
			width: 11,
			height: 11,
			radius: 6,
		},
		itemMargin: {
			horizontal: 12,
			vertical: 2
		},
		formatter: function(val, opts) {
			return val + ": " + opts.w.globals.series[opts.seriesIndex]
		},
		onItemClick: {
			toggleDataSeries: false
		},
		onItemHover: {
			highlightDataSeries: false
		},
	},
	dataLabels: {
		enabled: true,
		style: {
			fontSize: '11px',
			fontFamily: 'inherit',
			fontWeight: 400,
		},
		dropShadow: {
			blur: 8,
			opacity: 0.2
		}
	},
	tooltip: {
		fillSeriesColor: false,
		style: {
			fontSize: '14px',
			fontFamily: 'inherit',
		}
	},
	states: {
		hover: {
			filter: {
				type: 'none',
			}
		},
		active: {
			filter: {
				type: 'none',
			}
		}
	}
};

var optionsDashRadialBar01 = {
	series: [65],
	labels: ['unit'],
	chart: {
		type: 'radialBar',
		height: '100%',
	},
	colors: ['#5152f8', '#37d1a6'],
	plotOptions: {
		radialBar: {
			hollow: {
				size: '70%',
			},
			track: {
				background: '#f0f3f5',
				strokeWidth: '100%',
			},
			dataLabels: {
				name: {
					show: true,
					fontSize: '14px',
					fontFamily: 'inherit',
					fontWeight: 500,
					color: '#000000',
					offsetY: 20
				},
				value: {
					show: true,
					fontSize: '30px',
					fontFamily: 'inherit',
					fontWeight: 600,
					color: '#000000',
					offsetY: -13,
					formatter: function (val) {
						return val
						// return val + ' bytes'
					}
				}
			}
		},
	},
	stroke: {
    lineCap: "round",
  },
	states: {
		hover: {
			filter: {
				type: 'none',
			}
		},
		active: {
			filter: {
				type: 'none',
			}
		}
	}
};