{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of Decimal Numbers:1\n",
      "Enter 1 decimal numbers separated by space:7\n",
      "000\n"
     ]
    }
   ],
   "source": [
    "import itertools\n",
    "# Input Line 1 ( Asking for Number of Decimal Numbers)\n",
    "n=input(\"Number of Decimal Numbers:\")\n",
    "\n",
    "assert 1<=int(n)<=20\n",
    "\n",
    "\n",
    "#Input 2: Ask for decimal numbers separated by space\n",
    "numbers=input(\"Enter %s decimal numbers separated by space:\"%n)\n",
    "numbers=numbers.split(\" \")\n",
    "numbers=[int(number) for number in numbers]\n",
    "assert sum([1<i<10**5 for i in numbers])==len(numbers)==len(set(numbers))\n",
    "\n",
    "#Get no of bits for the maximum number\n",
    "max_bits=len(bin(max(numbers))[2:])\n",
    "\n",
    "#Possible sets using the numbers\n",
    "possible_sets=[]\n",
    "for i in range(1, len(numbers)+1):\n",
    "    for subset in itertools.combinations(numbers, i):\n",
    "        possible_sets.append(subset)\n",
    "\n",
    "# Equivalence Calculation \n",
    "equivalence=0\n",
    "for possible_set in possible_sets:\n",
    "    one_count=[bin(possible_set[i]).count('1') for i in range(len(possible_set))]\n",
    "    zero_count=[max_bits-bin(possible_set[i]).count('1') for i in range(len(possible_set))]\n",
    "    if(sum(zero_count)==sum(one_count)):\n",
    "        equivalence=equivalence+1\n",
    "\n",
    "output=bin(equivalence)[2:].zfill(max_bits)\n",
    "print(output)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
