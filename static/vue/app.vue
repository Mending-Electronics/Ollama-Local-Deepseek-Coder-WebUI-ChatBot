const app = Vue.createApp({
  data() {
      return {
          userInput: '',
          messages: [],
          loading: false,
          alertMessage: '',
          showAlertFlag: false
      };
  },
  methods: {
      async handleSubmit() {
          if (this.userInput.trim() === '') return;

          this.messages.push({ id: Date.now(), content: this.userInput, user: true });

          this.loading = true;

          const response = await fetch('/get_response', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ user_input: this.userInput }),
          });

          const data = await response.json();
          const botResponse = data.response;

          this.messages.push({ id: Date.now() + 1, content: botResponse, bot: true });

          this.loading = false;

          this.userInput = '';

          this.$nextTick(() => {
              const scrollableDiv = document.getElementById('scrollableDiv');
              scrollableDiv.scrollTop = scrollableDiv.scrollHeight;
          });
      },
      async copyToClipboard(message) {
          try {
              await navigator.clipboard.writeText(message);
              this.alertMessage = 'Message copied!';
              this.showAlert();
          } catch (err) {
              this.alertMessage = 'Failed to copy message!';
              this.showAlert();
          }
      },
      showAlert() {
          this.showAlertFlag = true;
          setTimeout(() => {
              this.showAlertFlag = false;
          }, 2000);
      },
      showButton(messageId) {
          const message = this.messages.find(msg => msg.id === messageId);
          if (message) {
              message.showButton = true;
          }
      },
      hideButton(messageId) {
          const message = this.messages.find(msg => msg.id === messageId);
          if (message) {
              setTimeout(() => {
                  message.showButton = false;
              }, 1000);
          }
      },
      renderMarkdown(content) {
          const markdownContent = marked.parse(content);
          return markdownContent;
      },
      createCodeCard(lang, code) {
          const card = document.createElement('div');
          card.className = 'card';

          const cardHeader = document.createElement('div');
          cardHeader.className = 'card-header d-flex justify-content-between align-items-center';
          cardHeader.innerHTML = `<span>${lang}</span><button class="btn btn-secondary btn-sm" onclick="app.copyCode(this)">Copy</button>`;
          card.appendChild(cardHeader);

          const cardBody = document.createElement('div');
          cardBody.className = 'card-body';
          cardBody.innerHTML = `<pre><code class="language-${lang}">${code}</code></pre>`;
          card.appendChild(cardBody);

          return card.outerHTML;
      },
      renderMessageContent(content) {
          const markdownContent = this.renderMarkdown(content);
          const tempDiv = document.createElement('div');
          tempDiv.innerHTML = markdownContent;

          const codeBlocks = tempDiv.querySelectorAll('pre code');
          codeBlocks.forEach(block => {
              const langMatch = block.className.match(/language-(\w+)/);
              const lang = langMatch ? langMatch[1] : 'unknown';
              const card = this.createCodeCard(lang, block.innerHTML);
              block.parentNode.outerHTML = card;
          });

          setTimeout(() => Prism.highlightAll(), 0);

          return tempDiv.innerHTML;
      },
      async copyCode(button) {
          try {
              const code = button.closest('.card').querySelector('pre code').textContent;
              await navigator.clipboard.writeText(code);
              
              // Change button text and add bg-success class
              const originalText = button.textContent;
              button.textContent = 'Copied !';
              button.classList.add('btn-success');

              // Revert button text and remove bg-success class after 3 seconds
              setTimeout(() => {
                  button.textContent = originalText;
                  button.classList.remove('btn-success');
              }, 3000);
          } catch (err) {
              console.error('Failed to copy code:', err);
          }
      }
  },
  mounted() {
      this.messages.forEach(message => {
          this.$set(message, 'showButton', false);
      });
  }
}).mount('#app');