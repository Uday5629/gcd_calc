import React, { useState } from 'react';
import './styles.css'; // Importing CSS file

function gcd(a, b) {
    // Euclidean algorithm to find GCD
    while (b !== 0) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function gcdOfArray(numbers) {
    if (numbers.length === 0) {
        return null; // No numbers provided
    }
    
    let result = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
        result = gcd(result, numbers[i]);
    }
    return result;
}

function GCDForm() {
    const [result, setResult] = useState(''); // State to store the result or error message

    const handleSubmit = (event) => {
        event.preventDefault(); // Prevent default form submission
        
        const inputNumbers = event.target.elements.numbers.value;
        const numbersArray = inputNumbers.split(",").map(Number); // Convert string input to array of numbers
        
        const gcdResult = gcdOfArray(numbersArray);
        if (gcdResult !== null) {
            // Update state to display the result
            setResult("GCD of " + inputNumbers + " is " + gcdResult);
        } else {
            // Update state to display an error message
            setResult("Please enter valid numbers");
        }
    };

    return (
        <div className="container">
            <h1>GCD Calculator</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="numbers">Enter numbers separated by commas:</label><br />
                <input type="text" id="numbers" name="numbers" /><br />
                <button type="submit">Calculate GCD</button>
            </form>
            {/* Display the result or error message */}
            <div className="result">{result}</div>
        </div>
    );
}

export default GCDForm; // Exporting the GCDForm component
