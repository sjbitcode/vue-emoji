<template>
	<header>
		<h1>{{ title }}</h1>
	</header>
</template>


<script>
	export default {
		props: {
			title: {
				type: String,
				required: true
			}
		},

		data() {
			return {

			}
		}
	}
</script>


<style>
	header {
		background: lightblue;
		padding: 10px;
	}

	h1 {
		color: #222;
		text-align: center;
	}
</style>