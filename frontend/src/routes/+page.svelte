<script lang="ts">
  import Quiz from '$lib/components/Quiz.svelte';
  let textInput = '';
  let urlInput = '';
  let isLoading = false;
  let quiz: any[] | null = null;
  let errorMessage: string | null = null;

  async function generateQuiz() {
    isLoading = true;
    errorMessage = null;
    quiz = null;

    try {
      const response = await fetch('http://localhost:8000/api/v1/quiz/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: textInput,
          url: urlInput,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to generate quiz');
      }

      quiz = await response.json();
    } catch (error) {
      errorMessage = error.message;
    } finally {
      isLoading = false;
    }
  }
</script>

<div class="space-y-8">
  <div class="bg-white p-8 rounded-lg shadow">
    <h2 class="text-2xl font-bold mb-6 text-gray-700">Generate a New Quiz</h2>
    <form on:submit|preventDefault={generateQuiz} class="space-y-4">
      <div>
        <label for="text-input" class="block text-sm font-medium text-gray-600">Paste your text</label>
        <textarea
          id="text-input"
          bind:value={textInput}
          rows="10"
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
          placeholder="Paste your notes, articles, or any text here..."
        ></textarea>
      </div>
      <div class="text-center text-gray-500">or</div>
      <div>
        <label for="url-input" class="block text-sm font-medium text-gray-600">Enter a URL</label>
        <input
          id="url-input"
          type="url"
          bind:value={urlInput}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
          placeholder="https://example.com"
        />
      </div>
      <div class="text-center">
        <button
          type="submit"
          class="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
          disabled={isLoading}
        >
          {isLoading ? 'Generating...' : 'Generate Quiz'}
        </button>
      </div>
    </form>
  </div>

  {#if errorMessage}
    <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
      <strong class="font-bold">Error:</strong>
      <span class="block sm:inline">{errorMessage}</span>
    </div>
  {:else if quiz}
    <Quiz {quiz} />
  {/if}
</div>
