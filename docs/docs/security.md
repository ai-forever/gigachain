<<<<<<< HEAD
# Безопасность

GigaChain позволяет интегрироваться со сторонними ресурсами такими как локальные и удаленные файловые системы, API и базы данных. Такой подход дает разработчикам создавать приложения, комбинирующие возможности больших языковых моделей (*LLM*) и работу со сторонними ресурсами.

## Лучшие практики

При разработке таких приложений следуйте лучшим практиками обеспечения безопасности:

* [**Ограничивайте права доступа**](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF_%D0%BC%D0%B8%D0%BD%D0%B8%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85_%D0%BF%D1%80%D0%B8%D0%B2%D0%B8%D0%BB%D0%B5%D0%B3%D0%B8%D0%B9). Предоставляйте приложениям только необходимые права. Расширенные или избыточные права создают угрозы безопасности. В зависимости от функциональности приложения используйте доступы с правами только на чтение, ограничьте доступ к чувствительным данным, запускайте приложение в контейнере.
* **Учитывайте возможность нецелевого использования**. При разработке приложения с LLM всегда помните, что сторонние ресурсы могут быть использованы настолько, насколько это позволяют сделать полученные права. Например, если права позволяют удалять данные из базы, лучше учитывать, что LLM с такими правами действительно может удалить данные.
* **Многоуровневая безопасность**. Не существует одного способа, который бы обеспечил полную безопасность. Тщательное проектирование цепочки и тонкая настройка не исключают возможных ошибок, которые могут совершать LLM. Поэтому, для обеспечения лучшей безопасности используйте различные подходы. Например, ограничивайте права приложения и запускайте его в контейнере, чтобы обеспечить доступ только к необходимым данным.

Несоблюдение описанных практик может привести к:

* повреждению или утрате данных;
* несанкционированному доступу к конфиденциальной информации;
* падению производительности, недоступности критических ресурсов и другим проблемам.

Примеры сценариев, которые описывают возможные пути предотвращения проблем:

* Если у агента есть доступ к файловой системе, пользователь может попросить его удалить файлы, не подлежащие удалению, или вывести содержимое файлов с конфиденциальной информацией. Чтобы избежать этого, ограничьте доступ агента определенной директорией и предоставьте ему права на работу только с теми файлами, с которыми работать безопасно. Рассмотрите возможность запуска приложения в контейнере.
* Если у агента есть доступ к стороннему API, пользователь может попросить удалить данные в API или передать ему вредоносные данные. Чтобы избежать этого, вы можете ограничить права агента только чтением данных или позволить агенту работать только с теми эндпоинтами, которые не допустят таких операций.
* Если у агента есть доступ к базе данных, пользователь может попросить удалить или мутировать таблицу. Чтобы избежать этого ограничьте доступ агента к таблицам и рассмотрите возможность выдать агенту учетные данные с доступом только на чтение.

При разработке приложений с доступом к различным внешним ресурсам вроде файловых систем, API или базам данных, проконсультируйтесь с ответственными за безопасность в вашей компании, чтобы понять, как лучше обеспечить безопасность ваших приложений.
=======
# Security

LangChain has a large ecosystem of integrations with various external resources like local and remote file systems, APIs and databases. These integrations allow developers to create versatile applications that combine the power of LLMs with the ability to access, interact with and manipulate external resources.

## Best practices

When building such applications developers should remember to follow good security practices:

* [**Limit Permissions**](https://en.wikipedia.org/wiki/Principle_of_least_privilege): Scope permissions specifically to the application's need. Granting broad or excessive permissions can introduce significant security vulnerabilities. To avoid such vulnerabilities, consider using read-only credentials, disallowing access to sensitive resources, using sandboxing techniques (such as running inside a container), etc. as appropriate for your application.
* **Anticipate Potential Misuse**: Just as humans can err, so can Large Language Models (LLMs). Always assume that any system access or credentials may be used in any way allowed by the permissions they are assigned. For example, if a pair of database credentials allows deleting data, it’s safest to assume that any LLM able to use those credentials may in fact delete data.
* [**Defense in Depth**](https://en.wikipedia.org/wiki/Defense_in_depth_(computing)): No security technique is perfect. Fine-tuning and good chain design can reduce, but not eliminate, the odds that a Large Language Model (LLM) may make a mistake. It’s best to combine multiple layered security approaches rather than relying on any single layer of defense to ensure security. For example: use both read-only permissions and sandboxing to ensure that LLMs are only able to access data that is explicitly meant for them to use.

Risks of not doing so include, but are not limited to:
* Data corruption or loss.
* Unauthorized access to confidential information.
* Compromised performance or availability of critical resources.

Example scenarios with mitigation strategies:

* A user may ask an agent with access to the file system to delete files that should not be deleted or read the content of files that contain sensitive information. To mitigate, limit the agent to only use a specific directory and only allow it to read or write files that are safe to read or write. Consider further sandboxing the agent by running it in a container.
* A user may ask an agent with write access to an external API to write malicious data to the API, or delete data from that API. To mitigate, give the agent read-only API keys, or limit it to only use endpoints that are already resistant to such misuse.
* A user may ask an agent with access to a database to drop a table or mutate the schema. To mitigate, scope the credentials to only the tables that the agent needs to access and consider issuing READ-ONLY credentials.

If you're building applications that access external resources like file systems, APIs
or databases, consider speaking with your company's security team to determine how to best
design and secure your applications.

## Reporting a vulnerability

Please report security vulnerabilities by email to security@langchain.dev. This will ensure the issue is promptly triaged and acted upon as needed.
>>>>>>> langchan/master
