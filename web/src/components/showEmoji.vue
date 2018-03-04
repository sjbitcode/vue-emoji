<template>
    <div class="container is-fluid">
            
    <div class="columns is-multiline is-mobile">
        <div v-for="emoji in emojis">
            <div class="emoji column" v-on:click="copy(emoji.shortcode)" :ref="'emoji_' + emoji.shortcode">
                {{ emoji.surrogate_pairs | format-code }}
            </div>
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

        data() {
            return {
                apples: [
                    'apple1', 'apple2', 'apple3',
                    'apple1', 'apple2', 'apple3',
                    'apple1', 'apple2', 'apple3',
                    'apple1', 'apple2', 'apple3',
                    'apple1', 'apple2', 'apple3',
                    'apple1', 'apple2', 'apple3',
                ]
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
    font-size: 6em;
    margin: 0 30px;
}
</style>