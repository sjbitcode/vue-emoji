<template>
	<div>
		<div v-for="emoji_category in emojis">
			<div v-for="val, key in emoji_category">
				<span @click="copy(key)">{{ key }}</span>
				<p v-show="val">{{ val }}</p>
			</div>
		</div>
	</div>
</template>


<script>
	export default {
		props: {
			emojis: {
				type: Object,
				required: true
			}
		},

		data() {
			return {
				
			}
		},

		methods: {
			copy: function(emoji) {
		      this.$clipboard(emoji);
		    }
		}
	}
</script>


<style>
	span {
		font-size:5rem;
		width:100%;
	}
</style>