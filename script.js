document.querySelector(".generate-btn").addEventListener("click", function () {
    const length = document.querySelector("input[type='range']").value;
    const useUppercase = document.querySelector("#uppercase").checked;
    const useNumbers = document.querySelector("#numbers").checked;
    const useSymbols = document.querySelector("#symbols").checked;
    const excludeDuplicate = document.querySelector("#exc-duplicate").checked;
    const includeSpaces = document.querySelector("#spaces").checked;

    const requestData = {
        length: parseInt(length),
        uppercase: useUppercase,
        numbers: useNumbers,
        symbols: useSymbols,
        exclude_duplicate: excludeDuplicate,
        spaces: includeSpaces,
    };

    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(requestData),
    })
        .then((response) => response.json())
        .then((data) => {
            document.querySelector(".input-box input").value = data.password;
        })
        .catch((error) => {
            console.error("Error:", error);
        });
});
