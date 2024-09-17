# Use the official MySQL image from Docker Hub
FROM mysql:8.0

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=ecommerce
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=password

# Copy the initialization script to the Docker container
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the default MySQL port
EXPOSE 3306

