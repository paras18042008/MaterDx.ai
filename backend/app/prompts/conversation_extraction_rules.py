EXTRACTION_RULES = """
Extract every clinically relevant piece of information.

Information categories include:

1. Symptoms
2. Symptom severity
3. Symptom duration
4. Symptom onset
5. Symptom location
6. Symptom radiation
7. Symptom progression
8. Aggravating factors
9. Relieving factors
10. Associated symptoms
11. Negated symptoms
12. Vital signs mentioned
13. Medical history
14. Surgical history
15. Family history
16. Medications
17. Allergies
18. Pregnancy information
19. Menstrual history
20. Lifestyle factors
21. Smoking
22. Alcohol
23. Recreational drugs
24. Occupation
25. Travel history
26. Animal exposure
27. Sick contacts
28. Recent procedures
29. Injuries
30. Timeline of events
31. Corrections to previous statements
32. Uncertain information

Never invent information.

Only extract information explicitly stated or clearly implied.

If information is missing, do not guess.

Preserve uncertainty.

Preserve negation.
"""