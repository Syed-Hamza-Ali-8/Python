import streamlit as st

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = []  # To store steps for visualization

    while low <= high:
        mid = (low + high) // 2
        steps.append(f"Checking middle index {mid}: {arr[mid]}")
        if arr[mid] == target:
            steps.append(f"Found {target} at index {mid}")
            return mid, steps
        elif arr[mid] < target:
            steps.append(f"{arr[mid]} < {target}, searching right half")
            low = mid + 1
        else:
            steps.append(f"{arr[mid]} > {target}, searching left half")
            high = mid - 1

    steps.append("Element not found")
    return -1, steps

st.title("🔍 Binary Search Visualizer")

user_input = st.text_input("Enter sorted numbers (comma-separated):", "1, 3, 5, 7, 9, 11")
target = st.number_input("Enter the number to search:", step=1)

if st.button("Search"):
    try:
        arr = list(map(int, user_input.split(',')))
        arr.sort()  # Ensure the array is sorted
        st.write("Sorted Array:", arr)
        index, steps = binary_search(arr, target)

        st.subheader("Search Steps:")
        for step in steps:
            st.write(step)
        
        if index != -1:
            st.success(f"Element found at index {index}")
        else:
            st.error("Element not found in the array")
    except ValueError:
        st.error("Please enter valid integers separated by commas.")
