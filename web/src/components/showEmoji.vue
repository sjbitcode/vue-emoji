<template>
    <div class="container is-fluid">

    <transition name="slither">  
        <div>
            &#x1F496;
        </div>
    </transition>
            
    <div class="columns is-multiline is-mobile">
        <div v-for="emoji in emojis">

            <b-tooltip class="my-tooltip" :label="tooltipText(emoji)">
                <div class="emoji column" v-on:click="copy(emoji.shortcode)" :ref="'emoji_' + emoji.shortcode">
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

            formatShortcode: function(str) {
                return ':' + str + ':'
            },

            tooltipText: function(emoji) {
                var text = this.formatShortcode(emoji.shortcode) + '\n' + emoji.shortened_codepoint;
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

.slither-enter-active, .slither-leave-active {
  transition: transform 3s;
}

.slither-enter, .slither-leave-to {
  transform: translateX(-100%);
}

.slither-enter-to, .slither-leave {
  transform: translateX(0);
}
</style>