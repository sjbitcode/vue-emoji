<template>
	<section class="hero is-medium">
		<div class="hero-body">
			<div class="container">

					<div class="columns">
						<div class="column is-3"></div>

						<div class="column">
							<div class="box">
								<div class="has-text-centered">
									<h1 class="title">Page Not Found</h1>
									<h2 class="subtitle">Sorry, the page you requested doesn't exist!</h2>

									<div class="ld ld-breath emoji" style="animation-duration:2.0s">{{ emoji }}</div>
								</div>
							</div>
						</div>

						<div class="column is-3"></div>
					</div>

			</div>
		</div>
	</section>
</template>


<script>
	export default {
		data() {
			return {
				emoji: '\ud83e\udd37\ud83c\udffb'
			}
		}
	}
</script>


<style scoped>
.emoji {
	font-size: 6em;
	margin-top: 10px;
}

.subtitle, .title {
	color: #7957d5 !important;
}

.subtitle {
	margin-top: 0 !important;
}

.hero {
	background-color: #ffffff;
	background-image: url("data:image/svg+xml,%3Csvg width='70' height='70' viewBox='0 0 70 70' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%237957d5' fill-opacity='0.15' fill-rule='evenodd'%3E%3Cpath d='M0 0h35v35H0V0zm5 5h25v25H5V5zm5 5h15v15H10V10zm5 5h5v5h-5v-5zM40 5h25v25H40V5zm5 5h15v15H45V10zm5 5h5v5h-5v-5zM70 35H35v35h35V35zm-5 5H40v25h25V40zm-5 5H45v15h15V45zm-5 5h-5v5h5v-5zM30 40H5v25h25V40zm-5 5H10v15h15V45zm-5 5h-5v5h5v-5z'/%3E%3C/g%3E%3C/svg%3E");
}
</style>