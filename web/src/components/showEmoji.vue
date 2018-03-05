<template>
    <div class="container is-fluid">
            
    <div class="columns is-multiline is-mobile">
        <div v-for="emoji in emojis">

            <b-tooltip class="my-tooltip" :label="tooltipText(emoji)">

                <div class="emoji column shake shake-freeze" v-on:click="copy(emoji.shortcode)" :ref="'emoji_' + emoji.shortcode">
                    <a>
                        {{ emoji.surrogate_pairs | format-code }}
                    </a>
                </div>

            </b-tooltip>
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

            formatShortcode: function(str) {
                return ':' + str + ':'
            },

            tooltipText: function(emoji) {
                var text = this.formatShortcode(emoji.shortcode);
                return text;
            }
        }
    }
</script>

<style scoped>
.emoji {
    font-size: 6em;
    margin: 0 30px;
}

.wiggle-enter-active {
  animation: bouncebody .5s;
}
.wiggle-leave-active {
  animation: bouncebody .5s reverse;
}
@keyframes bouncebody { 
  to { transform: scaleX(1.03) scaleY(0.97); } 
}
</style>