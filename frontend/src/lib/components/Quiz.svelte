<script lang="ts">
  export let quiz: any[];

  let currentQuestionIndex = 0;
  let userAnswers: (string | boolean | null)[] = [];
  let showResults = false;

  function handleAnswer(answer: string | boolean) {
    userAnswers[currentQuestionIndex] = answer;
    if (currentQuestionIndex < quiz.length - 1) {
      currentQuestionIndex++;
    } else {
      showResults = true;
    }
  }

  function resetQuiz() {
    currentQuestionIndex = 0;
    userAnswers = [];
    showResults = false;
  }
</script>

<div class="bg-white p-8 rounded-lg shadow">
  {#if !showResults}
    <div class="space-y-4">
      <h2 class="text-xl font-bold text-gray-700">
        Question {currentQuestionIndex + 1} of {quiz.length}
      </h2>
      <p class="text-gray-800">{quiz[currentQuestionIndex].question_text}</p>

      {#if quiz[currentQuestionIndex].question_type === 'multiple_choice'}
        <div class="space-y-2">
          {#each quiz[currentQuestionIndex].choices as choice}
            <button
              on:click={() => handleAnswer(choice)}
              class="block w-full text-left rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
            >
              {choice}
            </button>
          {/each}
        </div>
      {:else if quiz[currentQuestionIndex].question_type === 'true_false'}
        <div class="flex space-x-4">
          <button
            on:click={() => handleAnswer(true)}
            class="w-full rounded-md border border-transparent bg-green-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
          >
            True
          </button>
          <button
            on:click={() => handleAnswer(false)}
            class="w-full rounded-md border border-transparent bg-red-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
          >
            False
          </button>
        </div>
      {:else if quiz[currentQuestionIndex].question_type === 'descriptive'}
        <form on:submit|preventDefault={() => handleAnswer(userAnswers[currentQuestionIndex])}>
          <textarea
            bind:value={userAnswers[currentQuestionIndex]}
            rows="4"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            placeholder="Your answer..."
          ></textarea>
          <div class="mt-4 text-right">
            <button
              type="submit"
              class="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
            >
              Submit
            </button>
          </div>
        </form>
      {/if}
    </div>
  {:else}
    <div class="space-y-4">
      <h2 class="text-2xl font-bold text-gray-700">Quiz Results</h2>
      {#each quiz as question, i}
        <div class="border-t pt-4">
          <p class="font-semibold text-gray-800">{i + 1}. {question.question_text}</p>
          <p class="text-sm text-gray-600">Your answer: {userAnswers[i]}</p>
          <p class="text-sm text-green-600">Correct answer: {question.correct_answer}</p>
          <p class="text-sm text-gray-500">Explanation: {question.explanation}</p>
        </div>
      {/each}
      <div class="text-center">
        <button
          on:click={resetQuiz}
          class="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
        >
          Take Another Quiz
        </button>
      </div>
    </div>
  {/if}
</div>
