<template>
	<header>
		<section class="hero is-primary is-bold">
			<div class="hero-body">
				<div class="container has-text-centered">
					<h1 class="title">
						Emoji Index &#x1F64A;
					</h1>
					<h2 class="subtitle">
						search &amp; filter emoji
					</h2>
				</div>
			</div>
	</section>
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
	/*header {
		background: lightblue;
		padding: 10px;
	}

	h1 {
		color: #222;
		text-align: center;
	}*/
</style>