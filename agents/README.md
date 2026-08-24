# Agent Instructions

Agents are deliberately constrained specialist roles, not independent personalities. Before work, each role reads the shared rules and its role file. Every role file uses this contract:

1. **Role** and **Objective** define its narrow responsibility.
2. **Inputs**, **Allowed Reads**, and **Allowed Writes** bound access.
3. **Questions to Ask** identifies blocking and uncertainty checks.
4. **Method**, **Evidence Standard**, and **Confidence Rules** control reasoning.
5. **Must Not**, **Stop Conditions**, and **Escalation** constrain unsafe or unjustified action.
6. **Expected Output** and **Example** make work reviewable.

A role may propose changes outside its write boundary but cannot make them silently. Shared rules always apply; clinical-safety escalation overrides output completion.
