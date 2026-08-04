const steps = Array.from(document.querySelectorAll(".funnel-step"));

function showStep(nameOrNumber) {
  steps.forEach((step) => {
    const key = step.dataset.step;
    const match =
      key === String(nameOrNumber) ||
      (nameOrNumber === "done" && key === "done");
    step.hidden = !match;
  });
}

function currentStep() {
  return steps.find((s) => !s.hidden);
}

document.getElementById("funnel").addEventListener("click", (e) => {
  const t = e.target;
  if (!(t instanceof HTMLElement)) return;

  const current = currentStep();
  if (!current) return;
  const n = current.dataset.step;

  if (t.matches("[data-next]")) {
    if (n === "1") showStep(2);
    else if (n === "2") showStep(3);
  }

  if (t.matches("[data-back]")) {
    if (n === "2") showStep(1);
    else if (n === "3") showStep(2);
  }
});

document.getElementById("signup-form").addEventListener("submit", (e) => {
  e.preventDefault();
  // Später: an Backend / E-Mail-Tool senden
  showStep("done");
});

showStep(1);
