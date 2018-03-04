<template>
    <div>
        <div v-for="emoji in emojis">
            <div v-on:click="copy(emoji.shortcode)" :ref="'emoji_' + emoji.shortcode">
                {{ emoji.surrogate_pairs | format-code }}
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            emojis: {
                type: Array,
                required: true
            }
        },

        methods: {
            copy: function(shortcode) {
              // Find ref and copy to clipboard
              var ref_name = 'emoji_' + shortcode;
              this.$clipboard(this.$refs[ref_name][0].innerText);
            },
        }
    }
</script>

<style scoped>
.emoji {
    /*font-size: 5em;*/
}
</style>