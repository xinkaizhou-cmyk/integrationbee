easy_questions = [
    {
        "text": "∫ 2x cos(x^2) dx",
        "choices": ["sin(x^2) + C", "cos(x^2) + C", "x^2 cos(x^2) + C"],
        "answer": 0,
        "method": "Substitution"
    },
    {
        "text": "∫ e^x dx",
        "choices": ["e^x + C", "xe^x + C", "ln(x) + C"],
        "answer": 0,
        "method": "Direct Integration"
    },
    {
        "text": "∫ x e^x dx",
        "choices": ["e^x + C", "xe^x - e^x + C", "x^2 e^x + C"],
        "answer": 1,
        "method": "Integration by Parts"
    },
    {
        "text": "∫ x^2 dx",
        "choices": ["x^3/3 + C", "2x + C", "x^2/2 + C"],
        "answer": 0,
        "method": "Power Rule"
    },
    {
        "text": "∫ 4x dx",
        "choices": ["2x^2 + C", "4x^2 + C", "x^2 + C"],
        "answer": 0,
        "method": "Power Rule"
    },
    {
        "text": "∫ tan(x) dx",
        "choices": ["ln|sec(x)| + C", "-ln|cos(x)| + C", "sec(x)tan(x) + C"],
        "answer": 1,
        "method": "Basic Trig Integral"
    },
    {
        "text": "∫ cot(x) dx",
        "choices": ["ln|sin(x)| + C", "ln|cos(x)| + C", "-sec(x) + C"],
        "answer": 0,
        "method": "Basic Trig Integral"
    },
    {
        "text": "∫ sec(x)tan(x) dx",
        "choices": ["sec(x) + C", "tan(x) + C", "sec^2(x) + C"],
        "answer": 0,
        "method": "Basic Trig Integral"
    }
]
medium_questions = [
    {
        "text": "∫ x e^x dx",
        "choices": ["e^x + C", "xe^x - e^x + C", "x^2 e^x + C"],
        "answer": 1,
        "method": "Integration by Parts"
    },
    {
        "text": "∫ ln(x) dx",
        "choices": ["x ln(x) - x + C", "ln(x)/x + C", "x ln(x) + C"],
        "answer": 0,
        "method": "Integration by Parts"
    },
    {
        "text": "∫ x/(x^2 + 1) dx",
        "choices": ["ln(x^2+1) + C", "(1/2)ln(x^2+1) + C", "arctan(x) + C"],
        "answer": 1,
        "method": "u-Substitution"
    },
    {
        "text": "∫ e^(2x) dx",
        "choices": ["e^(2x) + C", "(1/2)e^(2x) + C", "2e^(2x) + C"],
        "answer": 1,
        "method": "u-Substitution"
    },
    {
        "text": "∫ 1/(x ln(x)) dx",
        "choices": ["ln|ln(x)| + C", "1/ln(x) + C", "ln(x)/x + C"],
        "answer": 0,
        "method": "u-Substitution"
    },
    {
        "text": "∫ x cos(x) dx",
        "choices": ["x sin(x) + cos(x) + C", "x sin(x) - cos(x) + C", "sin(x) + C"],
        "answer": 1,
        "method": "Integration by Parts"
    },
    {
        "text": "∫ sin(2x) dx",
        "choices": ["-cos(2x) + C", "-(1/2)cos(2x) + C", "(1/2)sin(2x) + C"],
        "answer": 1,
        "method": "u-Substitution"
    },
    {
        "text": "∫ 1/√(1-x^2) dx",
        "choices": ["arctan(x) + C", "arcsin(x) + C", "ln|x| + C"],
        "answer": 1,
        "method": "Inverse Trig"
    },
    {
        "text": "∫ x^2 ln(x) dx",
        "choices": ["(x^3/3)ln(x) - x^3/9 + C", "x^2/2 ln(x) + C", "ln(x^3) + C"],
        "answer": 0,
        "method": "Integration by Parts"
    },
    {
        "text": "∫ 1/(x^2 + 4) dx",
        "choices": ["(1/2)arctan(x/2) + C", "arctan(x^2) + C", "ln(x^2+4) + C"],
        "answer": 0,
        "method": "Inverse Trig"
    }
]
hard_questions = [
    {
        "text": "∫₀¹ ln(1+x)/(1+x²) dx",
        "choices": ["π ln(2)/8", "G", "π²/16"],
        "answer": 1,
        "method": "Symmetry/Substitution"
    },
    {
        "text": "∫₀¹ (x^a - 1)/ln(x) dx, a > -1",
        "choices": ["ln(a+1)", "1/(a+1)", "a"],
        "answer": 0,
        "method": "Feynman Technique"
    },
    {
        "text": "∫₀^∞ ln(x)/(1+x²) dx",
        "choices": ["0", "π/2", "-π/2"],
        "answer": 0,
        "method": "Symmetry"
    },
    {
        "text": "∫₀^(π/2) ln(sin x) dx",
        "choices": ["-π ln(2)/2", "-π ln(2)", "0"],
        "answer": 0,
        "method": "Symmetry"
    },
    {
        "text": "∫₀¹ x^m(1-x)^n dx, m,n > -1",
        "choices": ["Γ(m+1)Γ(n+1)/Γ(m+n+2)", "Γ(m+n+2)/(Γ(m+1)Γ(n+1))", "1/(m+n+1)"],
        "answer": 0,
        "method": "Beta Function"
    },
    {
        "text": "∫₀¹ arctan(x)/x dx",
        "choices": ["π/4", "G", "ln(2)"],
        "answer": 1,
        "method": "Series Expansion"
    },
    {
        "text": "∫₀^∞ x e^(-x²) dx",
        "choices": ["1/2", "1", "√π/2"],
        "answer": 0,
        "method": "Substitution"
    },
    {
        "text": "∫₀^∞ (e^(-ax) - e^(-bx))/x dx, a,b > 0",
        "choices": ["ln(b/a)", "ln(a/b)", "b-a"],
        "answer": 0,
        "method": "Frullani Integral"
    },
    {
        "text": "∫₀¹ ln²(x) dx",
        "choices": ["1", "2", "π²/6"],
        "answer": 1,
        "method": "Gamma Function"
    },
    {
        "text": "∫₀^∞ sin(x)/x dx",
        "choices": ["π", "π/2", "1"],
        "answer": 1,
        "method": "Dirichlet Integral"
    }
]